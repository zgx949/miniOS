from abc import ABC, abstractmethod

from fileSys.interface.engines.baidu import Baidu
from fileSys.interface.engines.localdisk import LocalDisk
from fileSys.models import FileIndexNode

# 协议与类映射
protocolMAP = {
    'localdisk': LocalDisk,
    'baidu': Baidu,
}


class InodeInterface(ABC):
    def __init__(self, iNode):
        self.iNode = iNode  # 载入索引节点信息

    @abstractmethod
    def read(self, size: int = -1) -> bytes:
        """
        抽象方法，从文件中读取数据。
        :param size: 要读取的字节数，默认为-1表示读取到文件结尾
        :return: 读取的数据
        """
        pass

    @abstractmethod
    def write(self, data: bytes):
        """
        抽象方法，向文件中写入数据。
        :param data: 要写入的数据
        """
        pass

    @abstractmethod
    def close(self):
        """
        抽象方法，关闭文件。
        """
        pass

    @abstractmethod
    def delete(self) -> bool:
        """
        抽象方法，删除索引块
        :return:
        """
        pass

    @abstractmethod
    def exists(self) -> bool:
        """
        索引块是否存在

        :return:
        """
        pass

    @staticmethod
    def parse_inode(inode: FileIndexNode):
        """
        把inode数据记录转为实际物理存储引擎
        inode由url组成 类名://路径
        例如：localdisk://blocks/123

        :param inode:
        :return:
        """

        # 获取引擎协议
        protocol, path = inode.path.split('://')[0]

        engine = protocolMAP.get(protocol, None)
        if engine is None:
            raise TypeError(f"Physical file system protocol is not defined")
        inode.path = path  # 把协议头去掉
        return engine(inode)
