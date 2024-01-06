package main

import (
	"context"
	"fmt"
	"github.com/gin-gonic/gin"
	"go.mongodb.org/mongo-driver/bson"
	"go.mongodb.org/mongo-driver/bson/primitive"
	"go.mongodb.org/mongo-driver/mongo"
	"go.mongodb.org/mongo-driver/mongo/options"
	"log"
	"net/http"
	"time"
)

var mongoClient *mongo.Client
var db *mongo.Database

// User 结构体定义
type User struct {
	ID        primitive.ObjectID `bson:"_id,omitempty"`
	Username  string             `bson:"username"`
	Password  string             `bson:"password"` // 实际应用中不推荐明文存储密码，这里仅作示例
	Email     string             `bson:"email"`
	CreatedAt time.Time          `bson:"created_at"`
}

func userTable() *mongo.Collection {
	return db.Collection("users")
}

func queryUser(c *gin.Context) {
	var user User
	username := c.Param("username")
	fmt.Printf("查询用户名：%s\n", username)
	err := userTable().FindOne(context.TODO(), bson.M{"username": username}).Decode(&user)
	if err != nil {
		fmt.Println(err)
		c.JSON(http.StatusOK, gin.H{
			"msg":  "账号不存在",
			"code": 1,
		})
		return
	}
	c.JSON(http.StatusOK, gin.H{
		"code": 0,
		"msg":  "ok",
		"data": user,
	})

}

func register(c *gin.Context) {
	var user User
	// 解析请求体
	if err := c.ShouldBindJSON(&user); err != nil {
		c.JSON(http.StatusOK, gin.H{
			"msg":  "请求错误",
			"code": 1,
		})
		return
	}
	// 检查账号是否重复
	err := userTable().FindOne(context.TODO(), bson.M{"username": user.Username}).Decode(&user)
	if err == nil {
		// 账号已存在
		c.JSON(http.StatusOK, gin.H{
			"msg":  "账号已存在",
			"code": 1,
		})
		return
	}
	// 新增数据
	res, _ := userTable().InsertOne(context.TODO(), user)
	c.JSON(http.StatusOK, gin.H{
		"msg":  "注册成功",
		"code": 0,
		"data": res,
	})
	//fmt.Printf("注册用户名：%s\n", username)

}

func login(c *gin.Context) {
	var user User
	// 解析请求体
	if err := c.ShouldBindJSON(&user); err != nil {
		c.JSON(http.StatusOK, gin.H{
			"msg":  "请求错误",
			"code": 1,
		})
		return
	}
	password := user.Password
	err := userTable().FindOne(context.TODO(), bson.M{"username": user.Username}).Decode(&user)
	if err != nil {
		// 账号不存在
		fmt.Println(err)
		c.JSON(http.StatusOK, gin.H{
			"msg":  "账号不存在",
			"code": 1,
		})
		return
	}
	// 验证账号密码
	if password == user.Password {
		c.JSON(http.StatusOK, gin.H{
			"code": 0,
			"msg":  "登录成功",
			"data": user,
		})
		return
	} else {
		c.JSON(http.StatusOK, gin.H{
			"code": 1,
			"msg":  "密码错误",
		})
	}

}

// FCB 结构体定义
type FCB struct {
	ID               primitive.ObjectID `bson:"_id,omitempty"`
	FileName         string             `bson:"fileName"`
	ParentID         primitive.ObjectID `bson:"parentId,omitempty"`
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
	return db.Collection("FCB")
}

func insertFCB(c *gin.Context) {
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

func folderList(c *gin.Context) {
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
func main() {
	// 初始化数据库
	mongoClient, _ = InitMongoClient()
	db = mongoClient.Database("minios")

	// 配置gin
	r := gin.Default()

	userGroup := r.Group("users")
	{
		userGroup.GET("/:username", queryUser)
		userGroup.POST("/register", register)
		userGroup.POST("/login", login)
	}

	fileGroup := r.Group("file")
	{
		fileGroup.POST("create", insertFCB)
		fileGroup.GET("list/:parentId", folderList)
	}

	r.Run(":8080") // 启动服务器

	// 断开连接
	err := mongoClient.Disconnect(context.TODO())
	if err != nil {
		log.Fatal(err)
	}
	fmt.Println("Connection to MongoDB closed.")
}

// InitMongoClient 返回一个新的MongoDB客户端实例。
func InitMongoClient() (*mongo.Client, error) {
	// 设置客户端连接配置
	clientOptions := options.Client().ApplyURI("mongodb://www.lefthand.top:27017")
	// 连接到MongoDB
	client, err := mongo.Connect(context.TODO(), clientOptions)
	if err != nil {
		log.Fatal(err)
	}
	// 检查连接
	err = client.Ping(context.TODO(), nil)
	if err != nil {
		log.Fatal(err)
	}
	fmt.Println("Connected to MongoDB!")
	return client, nil
}
