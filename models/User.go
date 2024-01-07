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

// User 结构体定义
type User struct {
	ID        primitive.ObjectID `bson:"_id,omitempty"`
	Username  string             `bson:"username"`
	Password  string             `bson:"password"` // 实际应用中不推荐明文存储密码，这里仅作示例
	Email     string             `bson:"email"`
	CreatedAt time.Time          `bson:"created_at"`
}

func userTable() *mongo.Collection {
	return config.GetDB().Collection("users")
}

// QueryUser 查询单个用户信息
func QueryUser(c *gin.Context) {
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

// Register 注册一个新用户
func Register(c *gin.Context) {
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

// Login 用户登录
func Login(c *gin.Context) {
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
