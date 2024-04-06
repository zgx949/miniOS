import logging
import os

from fileSys.interface.InodeInterface import InodeInterface


class LocalDisk(InodeInterface):

    def exists(self) -> bool:
        return os.path.exists(self.iNode.path)

    def delete(self) -> bool:
        if self.exists():
            os.remove(self.iNode.path)
        else:
            return False

    def read(self, size: int = -1) -> bytes:
        with open(f"./{self.iNode.path}", 'rb') as f:
            logging.info("正在读取文件块: %s", self.iNode.path)
            yield f.read()

    def write(self, block) -> bool:
        with open(f"./{self.iNode.path}", 'wb') as f:
            for chunk in block.chunks():
                f.write(chunk)
        return True

    def close(self):
        pass
