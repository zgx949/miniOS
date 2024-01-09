import re

from common.response import ErrorJsonMsg, NotLoginJsonMsg
from common.utils import requestBody2Json
from django.utils.deprecation import MiddlewareMixin

# 配置白名单路由
whiteListPath = ['/users/login', '/users/logout', '/users/register', '/admin/', '/admin']


# 全局请求拦截中间件
class RequestMiddleware(MiddlewareMixin):
    def process_request(self, request):
        if not request.user.is_authenticated:
            # 未登录
            whited = False
            for path in whiteListPath:
                # 正则匹配路由
                if re.match(path, request.path):
                    whited = True
                    break

            if not whited:
                # 未匹配到白名单路由
                return NotLoginJsonMsg(msg="未登录")

        if 'json' in request.content_type:
            # 请求体是json格式
            try:
                request.json_data = requestBody2Json(request)
            except Exception as e:
                return ErrorJsonMsg(msg="请求体JSON格式错误")

    def process_view(self, request, callback, callback_args, callback_kwargs):
        pass

    def process_response(self, request, response):
        return response
