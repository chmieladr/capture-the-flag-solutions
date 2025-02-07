import ctypes
import multiprocessing
import time

from Crypto.Cipher import AES

from classes import CipherMode, OperationMode, init_shared_data
from utils import get_mapper


def process_parallel(key: bytes, text: bytes,
                     cipher_mode: CipherMode,
                     op_mode: OperationMode = OperationMode.ENCRYPT,  # doesn't matter for CTR
                     init_args: tuple = tuple(),
                     num_processes: int = 4) -> bytes:
    block_size = AES.block_size
    no_blocks = int(len(text) / block_size)
    blocks = [range(i, no_blocks, num_processes) for i in range(num_processes)]

    shared_data = multiprocessing.RawArray(ctypes.c_ubyte, text)  # array containing the input data
    output_data = multiprocessing.RawArray(ctypes.c_ubyte, len(text))  # array for the output data of 'text's length

    pool = multiprocessing.Pool(num_processes, initializer=init_shared_data,
                                initargs=(shared_data, output_data, block_size, key, *init_args))
    start_time = time.time()

    mapper = get_mapper(cipher_mode, op_mode)
    if op_mode == OperationMode.ENCRYPT and cipher_mode == CipherMode.CBC:
        raise TypeError("CBC encryption mode not supported in parallel!")
    elif cipher_mode == CipherMode.CBC:
        pool.map(mapper, [(block, *init_args) for block in blocks])
    else:
        pool.map(mapper, blocks)

    mapper_name = f"{cipher_mode.name} {op_mode.name.lower() if cipher_mode != CipherMode.CTR else 'mode'}"
    print(f'{mapper_name} parallel time: {(time.time() - start_time): .4f} s')

    processed_text = bytes(output_data)
    return processed_text
