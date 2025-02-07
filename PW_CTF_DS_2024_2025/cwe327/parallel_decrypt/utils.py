from Crypto.Cipher import AES

from mappers import default_ctr_mapper, decrypt_cbc_mapper, decrypt_ecb_mapper, encrypt_ecb_mapper
from parallel import CipherMode, OperationMode


def nullpadding(data: bytes, length: int = AES.block_size) -> bytes:
    return data + b"\x00" * (length - len(data) % length)


def get_mapper(cipher_mode: CipherMode, op_mode: OperationMode):
    if cipher_mode == CipherMode.ECB:
        if op_mode == OperationMode.ENCRYPT:
            return encrypt_ecb_mapper
        else:
            return decrypt_ecb_mapper
    elif cipher_mode == CipherMode.CBC:
        if op_mode == OperationMode.ENCRYPT:
            raise TypeError("CBC encryption mode not supported in parallel!")
        else:
            return decrypt_cbc_mapper
    elif cipher_mode == CipherMode.CTR:
        return default_ctr_mapper
    raise TypeError("Invalid cipher mode!")


usage_message = """
Usage: python3 main.py <input_file> <output_file> <key> <mode> <iv/nonce>

<iv/nonce> is required only for CBC and CTR modes

Available modes:
1. ECB (encrypt)
2. ECB (decrypt)
3. CBC (encrypt) | not supported in parallel
4. CBC (decrypt)
5. CTR
"""

iv_message = """
IV is required for CBC mode

""" + usage_message

nonce_message = """
Nonce is required for CTR mode

""" + usage_message
