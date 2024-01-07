package main

import (
	"fileSys/config"
	"fileSys/router"
	"github.com/gin-gonic/gin"
)

func main() {
	// 初始化数据库
	config.InitMongoClient()
	config.SetDB("minios")
	// 配置gin
	r := gin.Default()

	// 用户路由组注册
	userGroup := r.Group("users")
	router.SetUserRouter(userGroup)

	// 文件路由组注册
	fileGroup := r.Group("file")
	router.SetFCBRouter(fileGroup)

	r.Run(":8080") // 启动服务器

	// 断开连接
	config.CloseDB()
}
