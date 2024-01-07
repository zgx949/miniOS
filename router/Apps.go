package router

import (
	"fileSys/models"
	"github.com/gin-gonic/gin"
)

type AppRouter struct {
	AppModels models.Apps
}

// SetAppsRouter  用户路由组注册
func SetAppsRouter(appsGroup *gin.RouterGroup) {
	appsGroup.POST("create", models.InsertApp)
	appsGroup.GET("list", models.AppList)
}
