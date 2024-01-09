from django.urls import path
from django.contrib import admin
from .api.apps import *

urlpatterns = [
    path('list', listApps),  # 列出所有应用
    path('create', createApp),  # 创建应用
    path('market', listAppsMarket),  # 列出应用市场所有应用
    path('install', installApp),  # 安装应用
]
