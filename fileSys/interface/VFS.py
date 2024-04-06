import os
import time

from common.utils import getFileMd5
from fileSys.interface.InodeInterface import InodeInterface
from fileSys.models import FileControlBlock, FileIndexNode
from django.db import transaction


class VFS:
    def mount(self, path: str, engine_config: dict):
        """
        抽象方法，用于挂载指定路径下的存储引擎，根据配置参数初始化。
        :param path: 存储位置的路径标识
        :param engine_config: 存储引擎所需的配置参数字典
        """
        pass

    def open(self, file_path: str, mode: str = 'r') -> any:
        """
        TODO:
        抽象方法，打开指定路径的文件。
        :param file_path: 文件路径
        :param mode: 打开模式（如'r'、'w'、'a'等）
        :return: 返回一个实现了File接口的对象
        """
        pass
    @staticmethod
    def mkdir(fileName, parentId, FileSize, owner) -> bool:
        """
        创建目录。
        :param fileName:
        :param parentId:
        :param FileSize:
        :param owner:
        """
        return VFS.create(fileName, 'folder', parentId, FileSize, owner)

    @staticmethod
    def listdir(id: str, owner: int) -> (list | str, bool):
        """
        抽象方法，列出指定目录下的文件和子目录列表。
        :param id: 目录路径的fcb id
        :param owner: 文件所有者
        :return: 包含文件和子目录名称的列表
        """
        if id == 'root':
            # 查询根目录
            data = FileControlBlock.objects.filter(parent_id=None, owner=owner)
            return data, True

        query = FileControlBlock.objects.filter(id=id)
        if query.exists():
            # 文件夹存在返回结果
            data = FileControlBlock.objects.filter(parent_id=id, owner=owner)
            return data, True
        return "文件夹不存在", False

    @staticmethod
    def read(id: int, FCB: FileControlBlock) -> bytes:
        """
        读取文件内容
        :param offset:
        :param file_path:
        :param mode:
        :return:
        """
        query = FileControlBlock.objects.filter(id=id)
        if not query.exists():
            yield "文件FCB不存在"
            return
        FCB = query.first()

        # 查询所有iNode节点
        iNodes = FileIndexNode.objects.filter(fcb=FCB)
        for inode in iNodes:
            physical_inode = InodeInterface.parse_inode(inode)
            physical_inode.read()

    def seek(self, offset: int, mode: str = 'r') -> bool:
        """
        头指针偏移
        :param offset:
        :param mode:
        :return:
        """
        pass

    @staticmethod
    def create(fileName, fileType, parentId, FileSize, owner) -> bool:
        """
        创建文件（夹）
        :param owner:
        :param FileSize:
        :param parentId:
        :param fileType:
        :param fileName:
        :return:
        """
        insertData = FileControlBlock.objects.create(
            file_name=fileName,
            file_type=fileType,
            parent_id=parentId,
            file_size=FileSize,
            owner=owner
        )
        return insertData

    @staticmethod
    def exists(fileName: str, fileType: str, parentId: int, owner: int) -> bool:
        """
        文件（夹）是否存在
        :param fileName:
        :param fileType:
        :param parentId:
        :param owner:
        :return:
        """
        # 检查FCB是否存在
        query = FileControlBlock.objects.filter(
            file_name=fileName,
            file_type=fileType,
            parent_id=parentId,
            owner=owner
        )
        return query.exists()

    @staticmethod
    def delete(id: int, owner: int) -> int:
        """
        删除文件
        :param id: FCB的Id
        :param owner: 文件权限拥有者
        :return:
        """
        delete_methods = []
        # 开启事务
        with transaction.atomic():
            # 删除FCB
            deleteList = [id]
            DeletedCount = 0
            # 广度优先删除
            while len(deleteList) > 0:
                # 查询子文件
                query = FileControlBlock.objects.filter(parent_id=deleteList[0], owner=owner)
                for item in query:
                    deleteList.append(item.id)

                # 查询出文件控制块
                FCB = FileControlBlock.objects.filter(id=deleteList[0], owner=owner).first()
                # 查询出文件索引节点
                inodes = FileIndexNode.objects.filter(fcb=FCB)
                for inode in inodes:
                    physical_inode = InodeInterface.parse_inode(inode)  # 解析为实际索引节点
                    if physical_inode.exists():  # 索引块存在
                        # 加入删除队列, 把函数指针传入，后面再统一删除
                        delete_methods.append(physical_inode.delete)

                    # 删除文件索引节点数据库记录
                    inode.delete()
                # 删除文件控制块
                count, _ = FCB.delete()
                DeletedCount += count
                # 删除列表中的第一个元素
                deleteList.pop(0)
        # 提交事务
        transaction.commit()
        # 执行删除文件物理块
        for delete_method in delete_methods:
            delete_method()

        return DeletedCount

    @staticmethod
    def write(FCBId: int, owner: int, block: bytes, index, blockMd5: str) -> bool:
        FCB = FileControlBlock.objects.get(id=FCBId, owner=owner)
        if not FCB:
            return False

        # 当没有传入md5时,生成md5
        if not blockMd5:
            blockMd5 = getFileMd5(block)

        # TODO：选择存储引擎
        blockName = f"localdisk://blocks/{int(time.time())}_{blockMd5}"
        size = block.size

        # 插入iNode节点
        iNode = FileIndexNode.objects.create(
            path=blockName,
            size=size,
            md5=blockMd5,
            index=index,
            fcb=FCB
        )

        # 新建一个物理节点
        physical_inode = InodeInterface.parse_inode(iNode)
        physical_inode.write(block)

        return iNode