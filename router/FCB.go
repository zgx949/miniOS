package router

import (
	"fileSys/models"
	"github.com/gin-gonic/gin"
)

type FCBRouter struct {
	UserModels models.User
}

// SetFCBRouter  FCB路由组注册
func SetFCBRouter(fileGroup *gin.RouterGroup) {
	fileGroup.POST("create", models.InsertFCB)
	fileGroup.GET("list/:parentId", models.FolderList)
	fileGroup.DELETE(":Id", models.DelFCB)
	fileGroup.POST("upload", models.UploadFile)
	fileGroup.GET("download/:Id", models.DownloadFile)
}
