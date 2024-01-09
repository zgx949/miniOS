"""
URL configuration for pyOS project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

# 导入路由组
from fileSys import urls as fileSys_urls
from apps import urls as apps_urls
from user import urls as user_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('file/', include(fileSys_urls)),    # 文件系统路由组
    path('app/', include(apps_urls)),      # 应用管理路由组
    path('users/', include(user_urls))      # 用户管理路由组
]
