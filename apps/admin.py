from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Apps)   # 注册应用模型
admin.site.register(UserApps)
admin.site.register(UserOpenedApps)
