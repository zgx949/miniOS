# 定义路由
from django.http import HttpResponseNotAllowed
from django.urls import path
from .api.FCB import *

# 路由列表
urlpatterns = [
    path('create', createFCB),  # 创建FCB
    path('list/<str:id>', openFolder),  # 打开文件夹
    path('delete', deleteFCB),  # 删除FCB
    path('upload', uploadFile),  # 上传文件
    path('download/<int:id>/<str:filename>', downloadFile),  # 下载文件
    path('open/<int:id>', openFile),  # 打开文件
]
