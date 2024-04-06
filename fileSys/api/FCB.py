import datetime
import os
import shutil

from django.db import transaction
from django.http import StreamingHttpResponse
from django.views.decorators.http import require_http_methods
from common import response as Response
from common.utils import requestBody2Json, getFileMd5
from fileSys.interface.VFS import VFS
from fileSys.models import *


@require_http_methods(['POST'])
def createFCB(request):
    """
    创建FCB :POST /file/create
    :param request:
    :return:
    """
    # 序列化数据
    json_data = request.json_data
    fileName = json_data.get('FileName')
    fileType = json_data.get('FileType')
    parentId = json_data.get('parentId')
    FileSize = json_data.get('FileSize', 0)
    owner = request.user.id

    VFS.exists(fileName, fileType, parentId, FileSize)

    if VFS.exists(fileName, fileType, parentId, FileSize):
        # FCB存在返回结果
        return Response.ErrorJsonMsg(msg="FCB已存在")
    insertData = VFS.create(fileName, fileType, parentId, FileSize, owner)
    # 返回结果
    return Response.SuccessJsonMsg(data=insertData)


@require_http_methods(['POST'])
def deleteFCB(request):
    """
    删除FCB :POST /file/{ID}
    :param request:
    :return:
    """
    owner = request.user.id
    id = request.json_data.get('id')
    DeletedCount = VFS.delete(id, owner)
    return Response.SuccessJsonMsg(msg="删除成功", data={"DeletedCount": DeletedCount})


@require_http_methods(['GET'])
def openFolder(request, id):
    """
    打开文件夹 :GET
    :param request:
    :return:
    """
    owner = request.user.id
    data, success = VFS.listdir(id, owner)
    # 返回结果
    return Response.SuccessJsonMsg(data=data) if success else Response.ErrorJsonMsg(msg="文件夹不存在")


@require_http_methods(['POST'])
def uploadFile(request):
    """
    上传文件 :POST /file/upload
    :param request:
    :return:
    """
    # 查询所在目录的FCB
    FCBId = request.POST.get('FCBId')
    owner = request.user.id

    # 接受文件块
    block = request.FILES.get('file')
    md5 = request.POST.get('md5')
    index = request.POST.get('chunkNumber')

    # 块校验
    blockMd5 = getFileMd5(block)
    if blockMd5 != md5:
        return Response.ErrorJsonMsg(msg="文件块校验失败")
    # 写文件块
    iNode = VFS.write(FCBId, owner, block, index, blockMd5)

    # 返回结果
    return Response.SuccessJsonMsg(msg="上传成功", data=iNode)


@require_http_methods(['GET'])
def downloadFile(request, id, filename):
    """
    下载文件 :GET /file/download/{ID}
    :param id: FCB的id
    :param filename: 自定义文件名，默认不处理
    :param request:
    :return:
    """

    # 检查FCB是否存在
    query = FileControlBlock.objects.filter(id=id)
    if not query.exists():
        return Response.ErrorJsonMsg(msg="文件FCB不存在")
    FCB = query.first()
    # 返回文件流
    response = StreamingHttpResponse(VFS.read(id, FCB))
    response['Content-Length'] = str(FCB.file_size)
    # 设置返回头
    response['Content-Type'] = 'application/octet-stream'
    # response['Content-Disposition'] = f'attachment;filename="{FCB.file_name}"'
    response['Content-Disposition'] = f'attachment; filename="{FCB.file_name}"; filename*=utf-8\'\'{FCB.file_name}'

    return response


def openFile(request, id):
    """
    TODO：修改到物理引擎中
    下载文件 :GET /file/download/{ID}
    :param request:
    :return:
    """
    # 块索引
    index = request.GET.get('index')

    # 检查FCB是否存在
    query = FileControlBlock.objects.filter(id=id)
    if not query.exists():
        return Response.ErrorJsonMsg(msg="文件FCB不存在")
    FCB = query.first()

    iNodes = []  # iNode节点
    if not index:
        # 查询所有iNode节点
        iNodes = FileIndexNode.objects.filter(fcb=FCB)
    else:
        # 查询指定iNode节点
        iNodes = FileIndexNode.objects.filter(fcb=FCB, index=index)

    def readBlocks():
        # 读取文件块
        for iNode in iNodes:
            with open(f"./blocks/{iNode.path}", 'rb') as f:
                yield f.read()

    # 返回文件流
    # 设置文件响应头
    response = StreamingHttpResponse(readBlocks())
    return response
