import time

from django.db import models

# Create your models here.

from django.db import models
from django.utils import timezone


class SystemOpenFileTable(models.Model):
    """
    系统打开文件表

    """
    file_id = models.CharField(max_length=255, unique=True)  # 文件ID：唯一标识每个文件的编号
    file_path = models.CharField(max_length=255)  # 文件路径：文件在系统中的存储路径
    file_name = models.CharField(max_length=255)  # 文件名：文件的名称
    creation_time = models.DateTimeField(default=timezone.now)  # 创建时间：文件被创建的时间
    modification_time = models.DateTimeField(auto_now=True)  # 修改时间：文件最后一次被修改的时间
    file_size = models.BigIntegerField()  # 文件大小：文件的大小
    other_attributes = models.JSONField()  # 其他属性：例如文件类型、权限等


class UserOpenFileTable(models.Model):
    """
    用户打开文件表

    """
    user_id = models.CharField(max_length=255, unique=True)  # 用户ID：唯一标识每个用户的编号
    file_id = models.ForeignKey(SystemOpenFileTable, on_delete=models.CASCADE)  # 文件ID：与系统打开文件表中的文件ID对应
    open_time = models.DateTimeField(default=timezone.now)  # 打开时间：用户打开文件的时间
    operation_status = models.CharField(max_length=255)  # 操作状态：表示用户对文件的操作状态，例如只读、读写等
    other_attributes = models.JSONField()  # 其他属性：例如光标位置、锁定状态等


class FileControlBlock(models.Model):
    """
    FCB文件控制块
    """
    file_name = models.CharField(max_length=255)  # 文件名
    file_size = models.BigIntegerField(null=True)  # 文件大小
    parent_id = models.IntegerField(null=True)  # 父目录ID
    creation_time = models.DateTimeField(auto_now_add=True, null=True)  # 创建时间
    modification_time = models.DateTimeField(auto_now=True, null=True)  # 修改时间
    permissions = models.CharField(max_length=10, null=True)  # 权限
    owner = models.IntegerField(null=True)  # 所有者
    group = models.IntegerField(null=True)  # 组
    file_type = models.CharField(max_length=255)  # 文件类型

    def __str__(self):
        return self.file_name


class FileIndexNode(models.Model):
    """
    文件索引节点表

    """
    path = models.CharField(max_length=255)  # 块路径
    index = models.BigIntegerField()  # 块索引
    size = models.BigIntegerField()  # 块大小
    creation_time = models.DateTimeField(auto_now_add=True)  # 创建时间
    modification_time = models.DateTimeField(auto_now=True)  # 修改时间
    md5 = models.CharField(max_length=255, null=True)  # 块md5
    # FCB的id
    fcb = models.ForeignKey(FileControlBlock, on_delete=models.CASCADE)

    def __str__(self):
        return self.path
