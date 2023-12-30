package main

import (
	"github.com/gin-gonic/gin"
	"net/http"
)

func main() {
	r := gin.Default()
	// 配置静态资源目录

	//r.GET("/api/open", func(c *gin.Context) {
	//	c.JSON(http.StatusOK, gin.H{
	//		"msg": "打开系统调用",
	//	})
	//})
	//
	//r.PUT("/api/create", func(c *gin.Context) {
	//	c.JSON(http.StatusOK, gin.H{
	//		"msg": "创建调用",
	//	})
	//})
	r.LoadHTMLGlob("templates/*")
	r.Static("/static", "./static")

	r.Any("/file/*path", func(c *gin.Context) {
		path := c.Param("path") // 获取匹配到的参数
		c.HTML(http.StatusOK, "index.html", gin.H{
			"path": path,
		})

	})

	r.Run(":8080")

}
