from fileSys.interface.InodeInterface import InodeInterface


class Baidu(InodeInterface):
    def exists(self) -> bool:
        pass

    def delete(self) -> bool:
        pass

    def read(self, size: int = -1) -> bytes:
        pass

    def write(self, data: bytes):
        pass

    def close(self):
        pass

