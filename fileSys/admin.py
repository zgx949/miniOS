from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(FileControlBlock)  # 注册文件控制块模型
admin.site.register(FileIndexNode)  # 注册文件索引节点模型
admin.site.register(SystemOpenFileTable)  # 注册系统打开文件表模型
admin.site.register(UserOpenFileTable)  # 注册用户打开文件表模型
