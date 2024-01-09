import datetime
import os

from django.db import transaction
from django.http import StreamingHttpResponse
from django.views.decorators.http import require_http_methods
from common import response as Response
from common.utils import requestBody2Json, getFileMd5
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
    # 检查FCB是否存在
    query = FileControlBlock.objects.filter(
        file_name=fileName,
        file_type=fileType,
        parent_id=parentId
    )

    if query.exists():
        # FCB存在返回结果
        return Response.ErrorJsonMsg(msg="FCB已存在")
    # 创建FCB
    insertData = FileControlBlock.objects.create(
        file_name=fileName,
        file_type=fileType,
        parent_id=parentId,
        file_size=FileSize
    )
    # 返回结果
    return Response.SuccessJsonMsg(data=insertData)


@require_http_methods(['POST'])
def deleteFCB(request):
    """
    删除FCB :POST /file/{ID}
    :param request:
    :return:
    """
    delPaths = []
    # 开启事务
    with transaction.atomic():
        # 删除FCB
        id = request.json_data.get('id')
        deleteList = [id]
        DeletedCount = 0
        # 广度优先删除
        while len(deleteList) > 0:
            # 查询子文件
            query = FileControlBlock.objects.filter(parent_id=deleteList[0])
            for item in query:
                deleteList.append(item.id)

            # 查询出文件控制块
            FCB = FileControlBlock.objects.filter(id=deleteList[0]).first()
            # 删除文件索引节点
            inodes = FileIndexNode.objects.filter(fcb=FCB)
            for inode in inodes:
                if os.path.exists(f"./blocks/{inode.path}"):
                    # 删除文件块
                    delPaths.append(f"./blocks/{inode.path}")
                # 删除文件索引节点
                inode.delete()
            # 删除文件控制块
            count, _ = FCB.delete()
            DeletedCount += count
            # 删除列表中的第一个元素
            deleteList.pop(0)
    # 提交事务
    transaction.commit()
    # 删除文件块
    for path in delPaths:
        if os.path.exists(path):
            os.remove(path)
    # 返回结果
    return Response.SuccessJsonMsg(msg="删除成功", data={"DeletedCount": DeletedCount})


@require_http_methods(['GET'])
def openFolder(request, id):
    """
    打开文件夹 :GET
    :param request:
    :return:
    """
    # 检查FCB是否存在
    if id == 'root':
        # 查询根目录
        data = FileControlBlock.objects.filter(parent_id=None)
        return Response.SuccessJsonMsg(data=data)

    query = FileControlBlock.objects.filter(id=id)
    if query.exists():
        # 文件夹存在返回结果
        data = FileControlBlock.objects.filter(parent_id=id)
        return Response.SuccessJsonMsg(data=data)

    # 返回结果
    return Response.ErrorJsonMsg("文件夹不存在")


@require_http_methods(['POST'])
def uploadFile(request):
    """
    上传文件 :POST /file/upload
    :param request:
    :return:
    """
    # 查询FCB
    FCBId = request.POST.get('FCBId')
    FCB = FileControlBlock.objects.get(id=FCBId)
    if not FCB:
        return Response.ErrorJsonMsg(msg="文件FCB不存在")

    # 接受文件块
    block = request.FILES.get('file')
    md5 = request.POST.get('md5')
    index = request.POST.get('chunkNumber')

    # 块校验
    blockMd5 = getFileMd5(block)
    if blockMd5 != md5:
        return Response.ErrorJsonMsg(msg="文件块校验失败")
    # 存储到文件系统
    blockName = f"{int(time.time())}_{blockMd5}"
    size = block.size
    with open(f"./blocks/{blockName}", 'wb') as f:
        for chunk in block.chunks():
            f.write(chunk)

    # 插入iNode节点
    iNode = FileIndexNode.objects.create(
        path=blockName,
        size=size,
        md5=blockMd5,
        index=index,
        fcb=FCB
    )

    # 返回结果
    return Response.SuccessJsonMsg(msg="上传成功", data=iNode)


@require_http_methods(['GET'])
def downloadFile(request, id):
    """
    下载文件 :GET /file/download/{ID}
    :param request:
    :return:
    """

    # 检查FCB是否存在
    query = FileControlBlock.objects.filter(id=id)
    if not query.exists():
        return Response.ErrorJsonMsg(msg="文件FCB不存在")
    FCB = query.first()
    # 查询所有iNode节点
    iNodes = FileIndexNode.objects.filter(fcb=FCB)

    def readBlocks():
        # 读取文件块
        for iNode in iNodes:
            with open(f"./blocks/{iNode.path}", 'rb') as f:
                yield f.read()

    # 返回文件流
    # 设置文件响应头
    response = StreamingHttpResponse(readBlocks())
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = f'attachment;filename="{FCB.file_name}"'
    return response


def openFile(request, id):
    """
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
