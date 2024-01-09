from django.views.decorators.http import require_http_methods

from apps.models import *
from common.response import *
from django.core import serializers


@require_http_methods(['GET'])
def listApps(request):
    """
    列出所有应用 :GET /app/list
    :param request:
    :return:
    """
    # 返回所有APP列表
    user_id = request.user.id
    user_apps = UserApps.objects.filter(user_id=user_id)
    apps = Apps.objects.filter(id__in=user_apps.values('app_id'))
    # apps = Apps.objects.all()
    return SuccessJsonMsg("获取成功", apps)


def listAppsMarket(request):
    """
    列出应用市场所有应用 :GET /app/market
    :param request:
    :return:
    """
    # 返回所有APP列表
    apps = Apps.objects.all()
    return SuccessJsonMsg("获取成功", apps)


def installApp(request):
    """
    安装应用 :get /app/install
    :param request:
    :return:
    """
    id = request.json_data.get('id')
    # 检查APP是否存在
    app = Apps.objects.get(id=id)
    if not app:
        return ErrorJsonMsg("应用不存在")
    # 检查APP是否已经安装
    user_id = request.user.id
    user_apps = UserApps.objects.filter(user_id=user_id, app_id=id)
    if user_apps:
        return ErrorJsonMsg("应用已安装")
    # 安装APP
    user_app = UserApps(user_id=user_id, app_id=id)
    user_app.save()

    # 返回结果
    return SuccessJsonMsg("安装成功")


@require_http_methods(['POST'])
def createApp(request):
    """
    创建应用 :POST /app/create
    :param request:
    :return:
    """
    # 检查APP是否存在

    # 创建APP

    # 返回结果

    pass
