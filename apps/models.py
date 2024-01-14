# Create your models here.
from django.db import models


class Apps(models.Model):
    """
    所有应用表
    """
    name = models.CharField(max_length=255, null=True)  # 应用名
    img = models.TextField(null=True)  # 应用图标
    url = models.CharField(max_length=255, null=True)  # 应用地址
    component = models.CharField(max_length=255, null=True)  # 应用组件
    width = models.CharField(max_length=255, null=True)  # 假设宽度是一个可表示为字符串的值
    description = models.TextField(null=True)  # 应用描述
    created_at = models.DateTimeField(auto_now_add=True)  # 创建时间

    def __str__(self):
        return self.name


class UserApps(models.Model):
    """
    用户安装的应用表
    """
    user_id = models.IntegerField(null=True)  # 用户id
    app_id = models.IntegerField(null=True)  # 应用id
    created_at = models.DateTimeField(auto_now_add=True)  # 创建时间

    def __str__(self):
        return self.user_id


class UserOpenedApps(models.Model):
    """
    用户打开的应用表
    """
    user_id = models.IntegerField(null=True)  # 用户id
    json_data = models.TextField(null=True)  # json数据
    created_time = models.DateTimeField(auto_now_add=True)  # 创建时间

    def __str__(self):
        return self.user_id
