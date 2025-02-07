from Crypto.Cipher import AES

from classes import multiprocessing_data


# CBC decryption mapper
def decrypt_cbc_mapper(args: tuple) -> int:
    blocks, iv = args
    iv = iv.encode()
    it = 0

    cipher_text = multiprocessing_data.shared_data
    plain_text = multiprocessing_data.output_data
    block_size = multiprocessing_data.block_size
    aes = AES.new(multiprocessing_data.key, AES.MODE_ECB)  # CBC requires manual handling of IV

    for it in blocks:
        offset = it * block_size
        block = cipher_text[offset:offset + block_size]
        decrypted_block = aes.decrypt(bytes(block))

        if it == 0:
            decrypted_block = bytes(a ^ b for a, b in zip(decrypted_block, iv))  # use provided IV for the first block
        else:
            prev_offset = (it - 1) * block_size  # the next blocks will use previous ciphertext blocks as IV
            prev_block = cipher_text[prev_offset:prev_offset + block_size]
            decrypted_block = bytes(a ^ b for a, b in zip(decrypted_block, prev_block))

        plain_text[offset:offset + block_size] = decrypted_block

    return it


# CTR mapper (encryption and decryption are the same)
def default_ctr_mapper(blocks: range) -> int:
    it = 0

    text = multiprocessing_data.shared_data
    output_text = multiprocessing_data.output_data
    block_size = multiprocessing_data.block_size
    key = multiprocessing_data.key
    nonce = multiprocessing_data.nonce
    aes = AES.new(key, AES.MODE_CTR, nonce=nonce)

    for it in blocks:
        offset = it * block_size
        block = text[offset:offset + block_size]
        processed_block = aes.encrypt(bytes(block))  # encrypt and decrypt are the same in CTR mode
        output_text[offset:offset + block_size] = processed_block

    return it


# ECB encryption mapper
def encrypt_ecb_mapper(blocks: range) -> int:
    it = 0

    plain_text = multiprocessing_data.shared_data
    cipher_text = multiprocessing_data.output_data
    block_size = multiprocessing_data.block_size
    aes = AES.new(multiprocessing_data.key, AES.MODE_ECB)

    for it in blocks:
        offset = it * block_size
        block = plain_text[offset:offset + block_size]
        encrypted_block = aes.encrypt(bytes(block))
        cipher_text[offset:offset + block_size] = encrypted_block

    return it


# ECB decryption mapper
def decrypt_ecb_mapper(blocks: range) -> int:
    it = 0

    cipher_text = multiprocessing_data.shared_data
    plain_text = multiprocessing_data.output_data
    block_size = multiprocessing_data.block_size
    aes = AES.new(multiprocessing_data.key, AES.MODE_ECB)

    for it in blocks:
        offset = it * block_size
        block = cipher_text[offset:offset + block_size]
        decrypted_block = aes.decrypt(bytes(block))
        plain_text[offset:offset + block_size] = decrypted_block

    return it
