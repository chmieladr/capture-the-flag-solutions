from Crypto.Random import get_random_bytes
from Crypto.Protocol.KDF import PBKDF2
from Crypto.Cipher import AES
from PIL import Image

from bmp_crypt import nullpadding, convert_to_rgb


def decrypt_full(input_filename, mode, key):
    img_in = open(input_filename, "rb")
    data = img_in.read()

    data_padded = nullpadding(data)

    if mode == "CBC":
        iv = PBKDF2("Adrian123", b"grass")
        # iv = get_random_bytes(16)
        aes = AES.new(key, AES.MODE_CBC, iv)
    elif mode == "ECB":
        aes = AES.new(key, AES.MODE_ECB)
    else:
        raise ValueError("Invalid mode!")

    decrypted_data = aes.decrypt(data_padded)
    decrypted_data_unpadded = decrypted_data[:len(data)]

    name = ''.join(input_filename.split('_')[:-3])
    img_format = str(input_filename.split('.')[-1]).split('_')[0]

    output_filename = name + '_' + mode + '_decrypted_full.' + img_format

    img_out = open(output_filename, "wb")
    img_out.write(decrypted_data_unpadded)

    img_out.close()
    img_in.close()


def decrypt_data(input_filename: str, mode: str, key: str | bytes):
    img_in = Image.open(input_filename)
    data = img_in.convert("RGB").tobytes()

    data_padded = nullpadding(data)

    if mode == "CBC":
        iv = get_random_bytes(16)
        aes = AES.new(key, AES.MODE_CBC, iv)
    elif mode == "ECB":
        aes = AES.new(key, AES.MODE_ECB)
    else:
        raise ValueError("Invalid mode!")

    decrypted_data = aes.decrypt(data_padded)
    decrypted_data_unpadded = decrypted_data[:len(data)]

    img_out = Image.new(img_in.mode, img_in.size)
    img_out.putdata(convert_to_rgb(decrypted_data_unpadded))

    name = ''.join(input_filename.split('_')[:-2])
    img_format = str(input_filename.split('.')[-1])

    output_filename = name + '_' + mode + '_decrypted.' + img_format

    img_out.save(output_filename, img_format)
