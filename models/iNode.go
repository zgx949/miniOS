package models

import (
	"context"
	"fileSys/config"
	"go.mongodb.org/mongo-driver/bson/primitive"
	"go.mongodb.org/mongo-driver/mongo"
	"mime/multipart"
)

// FileIndexNode 文件索引结点结构体
type FileIndexNode struct {
	ID    primitive.ObjectID   `bson:"_id,omitempty"`
	Block multipart.FileHeader `bson:"block"`
}

func InodeTable() *mongo.Collection {
	return config.GetDB().Collection("inode")
}

// InsertInode 插入索引结点
func InsertInode(inode FileIndexNode) primitive.ObjectID {
	result, _ := InodeTable().InsertOne(context.TODO(), inode)
	return result.InsertedID.(primitive.ObjectID)
}

// GetInode 获取索引结点
func GetInode(id primitive.ObjectID) FileIndexNode {
	var inode FileIndexNode
	InodeTable().FindOne(context.TODO(), map[string]interface{}{
		"_id": id,
	}).Decode(&inode)
	return inode
}
