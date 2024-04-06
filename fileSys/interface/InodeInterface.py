from abc import ABC, abstractmethod


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


