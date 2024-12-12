from sys import argv

from Crypto.Protocol.KDF import PBKDF2

from bmp_crypt import encrypt_data, encrypt_full
from bmp_decrypt import decrypt_data, decrypt_full

if __name__ == "__main__":
    file = argv[1] + '.bmp'
    key = PBKDF2("Adrian123", b"salt")

    # Szyfrowanie samego obrazka
    encrypt_data(file, "ECB", key)
    encrypt_data(file, "CBC", key)

    # Szyfrowanie całego pliku wraz z nagłówkiem
    encrypt_full(file, "ECB", key)
    encrypt_full(file, "CBC", key)

    ecb = file[:-4] + "_ECB_encrypted.bmp"
    cbc = file[:-4] + "_CBC_encrypted.bmp"

    # Deszyfrowanie samego obrazka
    decrypt_data(ecb, "ECB", key)
    decrypt_data(cbc, "CBC", key)

    ecb = file[:-4] + "_ECB_encrypted_full.bmp"
    cbc = file[:-4] + "_CBC_encrypted_full.bmp"

    # Deszyfrowanie całego pliku wraz z nagłówkiem
    decrypt_full(ecb, "ECB", key)
    decrypt_full(cbc, "CBC", key)
