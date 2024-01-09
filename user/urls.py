# 定义路由
from django.http import HttpResponseNotAllowed
from django.urls import path
from .api.user import *

# 路由列表
urlpatterns = [
    path('login', UserLogin),  # 用户登录
    path('logout', UserLogout),  # 用户退出登录
    path('info', getUserInfo),  # 用户信息
    path('register', userRegister),  # 用户注册
]
