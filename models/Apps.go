package models

import (
	"context"
	"fileSys/config"
	"fmt"
	"github.com/gin-gonic/gin"
	"go.mongodb.org/mongo-driver/bson"
	"go.mongodb.org/mongo-driver/bson/primitive"
	"go.mongodb.org/mongo-driver/mongo"
	"net/http"
	"time"
)

// Apps 结构体定义
type Apps struct {
	ID        primitive.ObjectID `bson:"_id,omitempty"`
	Name      string             `bson:"name"`
	Img       string             `bson:"img"`
	Url       string             `bson:"url"`
	Component string             `bson:"component"`
	Width     string             `bson:"width"`
	CreatedAt time.Time          `bson:"created_at"`
}

func AppTable() *mongo.Collection {
	return config.GetDB().Collection("apps")
}

func AppList(c *gin.Context) {
	var results []bson.M
	var data bson.M

	cursor, err := AppTable().Find(context.TODO(), data)
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
		"msg":  "应用获取成功",
		"code": 0,
		"data": results,
	})

}

func InsertApp(c *gin.Context) {
	var app Apps
	// 解析请求体
	if err := c.ShouldBindJSON(&app); err != nil {
		c.JSON(http.StatusOK, gin.H{
			"msg":  "请求错误",
			"code": 1,
		})
		return
	}
	fmt.Println(app)
	// 新增数据
	res, _ := AppTable().InsertOne(context.TODO(), app)
	c.JSON(http.StatusOK, gin.H{
		"msg":  "App创建成功",
		"code": 0,
		"data": res,
	})
}
