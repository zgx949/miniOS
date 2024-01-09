import json
from django.core import serializers
from django.http import JsonResponse
from django.db.models.query import QuerySet
from django.forms.models import model_to_dict
import django.db.models


class StatusCodes:
    """
    错误状态码
    """
    SUCCESS = 0  # 成功
    Error = 1  # 失败
    NotLogin = -1  # 没登陆
    BAD_REQUEST = 400
    NOT_FOUND = 404
    INTERNAL_SERVER_ERROR = 500


def query2dict(query):
    """
    把序列化的数据转为普通对象

    :param query:
    :return:
    """
    temp = query['fields']
    temp['id'] = query['pk']
    return temp


def arr2obj(arr):
    """
    把序列化的数据转为普通对象

    :param arr:
    :return:
    """
    temp = []
    for item in arr:
        temp.append(query2dict(item))
    return temp


def tansformQueryData(data):
    """
    把QuerySet转为普通对象

    :param data:
    :return:
    """
    res_data = data
    if type(data) == QuerySet:
        # QuerySet对象需要序列化
        json_str = serializers.serialize('json', data)
        res_data = json.loads(json_str)

        if type(res_data) == list:
            # 结构化数据
            res_data = arr2obj(res_data)
        elif type(res_data) == dict:
            # 结构化数据
            res_data = query2dict(res_data)
    elif isinstance(data, django.db.models.Model):
        # 是django模型类型对象，转换为字典类型
        res_data = model_to_dict(data)

    return res_data


def SuccessJsonMsg(msg="OK", data=None):
    # 转换为结构化数据
    res_data = tansformQueryData(data)
    return JsonResponse({
        "msg": msg,
        "code": StatusCodes.SUCCESS,
        "data": res_data
    })


def ErrorJsonMsg(msg="请求错误", data=None):
    # 转换为结构化数据
    res_data = tansformQueryData(data)
    return JsonResponse({
        "msg": msg,
        "code": StatusCodes.Error,
        "data": res_data
    })


def NotLoginJsonMsg(msg="账号未登录", data=None):
    return JsonResponse({
        "msg": msg,
        "code": StatusCodes.NotLogin,
        "data": data
    })
