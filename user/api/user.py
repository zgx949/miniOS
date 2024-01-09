from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.views.decorators.http import require_http_methods

from apps.models import UserApps
from common.response import ErrorJsonMsg, SuccessJsonMsg


@require_http_methods(['POST'])
def UserLogin(request):
    """
    用户登录
    :param request:
    :return:
    """
    username = request.json_data.get("username")
    password = request.json_data.get("password")
    user = authenticate(request, username=username, password=password)
    if user is not None:
        # 记录登录状态
        login(request, user)
        return SuccessJsonMsg("登录成功", user)
    else:
        return ErrorJsonMsg("用户名或密码错误或用户不存在")


@require_http_methods(['POST'])
def UserLogout(request):
    """
    用户退出登录
    :param request:
    :return:
    """
    logout(request)
    return SuccessJsonMsg("退出登录成功")


def getUserInfo(request):
    """
    获取用户信息
    :param request:
    :return:
    """
    user = request.user
    return SuccessJsonMsg(data=user)


def userRegister(request):
    """
    用户注册
    :param request:
    :return:
    """
    username = request.json_data.get("username")
    password = request.json_data.get("password")
    email = request.json_data.get("email")
    if username is None or password is None or email is None:
        return ErrorJsonMsg("用户名或密码或邮箱不能为空")
    if User.objects.filter(username=username).exists():
        return ErrorJsonMsg("用户名已存在")
    # if User.objects.filter(email=email).exists():
    #     return ErrorJsonMsg("邮箱已存在")
    user = User.objects.create_user(username=username, password=password, email=email)
    user.save()
    # 安装默认app应用
    UserApps.objects.create(user_id=user.id, app_id=1)
    UserApps.objects.create(user_id=user.id, app_id=2)
    return SuccessJsonMsg("注册成功", user)
