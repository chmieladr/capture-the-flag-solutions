from enum import Enum

from Crypto.Cipher import AES


class CipherMode(Enum):
    ECB = AES.MODE_ECB
    CBC = AES.MODE_CBC
    CTR = AES.MODE_CTR


class OperationMode(Enum):
    ENCRYPT = 1
    DECRYPT = 2


class MPData:
    shared_data: bytes
    output_data: bytes
    block_size: int
    key: bytes
    iv: bytes
    nonce: bytes


multiprocessing_data = MPData()


def init_shared_data(shared_data: bytes, output_data: bytes, block_size: int, key: bytes, *args):
    global multiprocessing_data
    multiprocessing_data.shared_data = shared_data
    multiprocessing_data.output_data = output_data
    multiprocessing_data.block_size = block_size
    multiprocessing_data.key = key
    multiprocessing_data.iv = args[0] if args else None
    multiprocessing_data.nonce = args[0] if args else None