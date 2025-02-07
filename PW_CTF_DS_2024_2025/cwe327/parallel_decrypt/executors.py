# CBC encryption (not parallel! - added mostly for easier testing)
from Crypto.Cipher import AES

from classes import CipherMode, OperationMode
from parallel import process_parallel
from utils import nullpadding


def encrypt_cbc(key: bytes, plain_text: bytes, iv: str) -> bytes:
    aes = AES.new(key, AES.MODE_CBC, iv=iv.encode())

    padded_text = nullpadding(plain_text)

    encrypted_text = aes.encrypt(padded_text)
    return encrypted_text[:len(plain_text)]


# CBC decryption
def decrypt_cbc_parallel(key: bytes, text: bytes, iv: str, num_processes: int = 4) -> bytes:
    return process_parallel(key, text,
                            cipher_mode=CipherMode.CBC,
                            op_mode=OperationMode.DECRYPT,
                            init_args=(iv,),
                            num_processes=num_processes)


# CTR (encryption and decryption are the same)
def process_ctr_parallel(key: bytes, text: bytes, nonce: bytes, num_processes: int = 4) -> bytes:
    return process_parallel(key, text,
                            cipher_mode=CipherMode.CTR,
                            init_args=(nonce,),
                            num_processes=num_processes)


# ECB encryption
def encrypt_ecb_parallel(key: bytes, plain_text: bytes, num_processes: int = 4) -> bytes:
    return process_parallel(key, plain_text,
                            cipher_mode=CipherMode.ECB,
                            op_mode=OperationMode.ENCRYPT,
                            num_processes=num_processes)


# ECB decryption
def decrypt_ecb_parallel(key: bytes, cipher_text: bytes, num_processes: int = 4) -> bytes:
    return process_parallel(key, cipher_text,
                            cipher_mode=CipherMode.ECB,
                            op_mode=OperationMode.DECRYPT,
                            num_processes=num_processes)
