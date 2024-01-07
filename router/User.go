package router

import (
	"fileSys/models"
	"github.com/gin-gonic/gin"
)

type UserRouter struct {
	UserModels models.User
}

// SetUserRouter 用户路由组注册
func SetUserRouter(userGroup *gin.RouterGroup) {
	userGroup.GET("/:username", models.QueryUser)
	userGroup.POST("/register", models.Register)
	userGroup.POST("/login", models.Login)
}
