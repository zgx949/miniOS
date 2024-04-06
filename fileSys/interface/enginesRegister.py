from fileSys.interface.engines.baidu import Baidu
from fileSys.interface.engines.localdisk import LocalDisk
from fileSys.models import FileIndexNode

# 协议与类映射
protocolMAP = {
    'localdisk': LocalDisk,
    'baidu': Baidu,
}

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