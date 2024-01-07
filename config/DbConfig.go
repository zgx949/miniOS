package config

import (
	"context"
	"fmt"
	"go.mongodb.org/mongo-driver/mongo"
	"go.mongodb.org/mongo-driver/mongo/options"
	"log"
)

var (
	mongoClient *mongo.Client
	db          *mongo.Database
)

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
	fmt.Println("连接MongoDB成功!")
	return client, nil
}

func SetDB(Database string) *mongo.Database {
	// 初始化数据库
	mongoClient, _ = InitMongoClient()
	db = mongoClient.Database(Database)
	return db
}

func CloseDB() {
	// 断开连接
	err := mongoClient.Disconnect(context.TODO())
	if err != nil {
		log.Fatal(err)
	}
	fmt.Println("MongoDB已断开连接")
}

func GetDB() *mongo.Database {
	return db
}
