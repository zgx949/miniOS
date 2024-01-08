package models

import (
	"context"
	"fileSys/config"
	"fmt"
	"github.com/gin-gonic/gin"
	"go.mongodb.org/mongo-driver/bson"
	"go.mongodb.org/mongo-driver/bson/primitive"
	"go.mongodb.org/mongo-driver/mongo"
	"go.mongodb.org/mongo-driver/mongo/options"
	"net/http"
	"time"
)

// FCB 结构体定义
type FCB struct {
	ID               primitive.ObjectID `bson:"_id,omitempty"`
	FileName         string             `bson:"fileName"`
	ParentID         primitive.ObjectID `bson:"parentId,omitempty"`
	Inodes           []string           `bson:"inodes"`
	FileSize         int64              `bson:"fileSize"`
	CreationTime     time.Time          `bson:"creationTime"`
	ModificationTime time.Time          `bson:"modificationTime"`
	Permissions      string             `bson:"permissions"`
	Owner            int                `bson:"owner"`
	Group            int                `bson:"group"`
	FileType         string             `bson:"fileType"`
	FileLocation     int64              `bson:"fileLocation"`
	InodeNumber      int                `bson:"inodeNumber"`
}

func FCBTable() *mongo.Collection {
	return config.GetDB().Collection("FCB")
}

func InsertFCB(c *gin.Context) {
	// 检查是否有重复的文件
	var fcb FCB
	var temp FCB
	// 解析请求体
	if err := c.ShouldBindJSON(&fcb); err != nil {
		c.JSON(http.StatusOK, gin.H{
			"msg":  "请求错误",
			"code": 1,
		})
		return
	}
	// 检查fcb是否重复
	var data bson.M

	if fcb.ParentID.IsZero() {
		// 上级ID为空
		data = bson.M{
			"fileName": fcb.FileName,
			"fileType": fcb.FileType,
			"parentId": bson.M{"$eq": nil},
		}
	} else {
		// 有上一级ID
		data = bson.M{
			"fileName": fcb.FileName,
			"parentId": fcb.ParentID,
			"fileType": fcb.FileType,
		}
	}

	err := FCBTable().FindOne(
		context.TODO(),
		data).Decode(&temp)

	if err == nil {
		// FCB已存在
		c.JSON(http.StatusOK, gin.H{
			"msg":  "文件或文件夹已存在",
			"code": 1,
		})
		return
	}
	// 新增数据
	res, _ := FCBTable().InsertOne(context.TODO(), fcb)
	c.JSON(http.StatusOK, gin.H{
		"msg":  "文件（夹）创建成功",
		"code": 0,
		"data": res,
	})
}

func FolderList(c *gin.Context) {
	parentId := c.Param("parentId")
	fmt.Println("查询文件夹ID：", parentId)
	// 设置排序选项，按 fileType 字段升序排序
	sortOption := options.Find().SetSort(bson.D{{"fileType", 1}})

	var results []bson.M
	var data bson.M

	if parentId == "root" {
		// 查询根目录
		data = bson.M{"parentId": nil}
	} else {
		// 查询的文件夹
		id, _ := primitive.ObjectIDFromHex(parentId)
		fmt.Println("转换后的ID：", id)
		data = bson.M{"parentId": id}

	}

	cursor, err := FCBTable().Find(context.TODO(), data, sortOption)
	if err != nil {
		fmt.Println(err)
	}

	if err = cursor.All(context.TODO(), &results); err != nil {
		c.JSON(http.StatusOK, gin.H{
			"msg":  err,
			"code": 1,
			"data": results,
		})
		return
	}

	c.JSON(http.StatusOK, gin.H{
		"msg":  "文件（夹）获取成功",
		"code": 0,
		"data": results,
	})

}

// DelFCB 删除FCB
func DelFCB(c *gin.Context) {
	// 获取文件ID
	Id := c.Param("Id")
	ID, err := primitive.ObjectIDFromHex(Id)
	// 解析请求体
	if err != nil {
		c.JSON(http.StatusOK, gin.H{
			"msg":  "请求错误",
			"code": 1,
		})
		return
	}

	// 构造查询条件
	var data bson.M
	data = bson.M{
		"_id": ID,
	}

	// 删除当前FCB
	res, err := FCBTable().DeleteOne(
		context.TODO(),
		data)

	if err != nil {
		// 删除出错
		c.JSON(http.StatusOK, gin.H{
			"msg":  err,
			"code": 1,
		})

	} else {
		c.JSON(http.StatusOK, gin.H{
			"msg":  "删除成功",
			"code": 0,
			"data": res,
		})
	}
	// TODO: 删除Inode节点
	// TODO：删除该FCB的子目录及Inode节点

}

func UploadFile(c *gin.Context) {
	// 获取文件ID
	FCBId, _ := c.GetPostForm("FCBId")
	id, _ := primitive.ObjectIDFromHex(FCBId)
	// 读取文件块
	block, _ := c.FormFile("file")

	// md5校验

	//var results []bson.M
	var fcb FCB
	// 查询出FCB
	err := FCBTable().FindOne(context.TODO(), bson.M{"_id": id}).Decode(&fcb)
	if err != nil {
		// FCB不存在
		fmt.Println(err)
		c.JSON(http.StatusOK, gin.H{
			"msg":  "文件FCB不存在",
			"code": 1,
		})
		return
	}

	// 插入Inode
	// 生成当前时间的时间戳字符串
	timestamp := fmt.Sprintf("%d", time.Now().Unix())
	err = c.SaveUploadedFile(block, "./blocks/"+timestamp)

	if err != nil {
		c.JSON(http.StatusOK, gin.H{
			"msg":  "文件块上传失败",
			"code": 1,
			"data": fcb,
		})
		return
	}
	// 插入节点
	fcb.Inodes = append(fcb.Inodes, timestamp)

	// 更新FCB,插入Inode节点名
	FCBTable().UpdateOne(
		context.TODO(),
		bson.M{"_id": id},
		bson.M{
			"$set": bson.M{
				"inodes": fcb.Inodes,
			},
		})

	c.JSON(http.StatusOK, gin.H{
		"msg":  "文件块上传成功",
		"code": 0,
		"data": fcb,
	})

}
