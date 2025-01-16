from binascii import unhexlify

from Crypto.Cipher import AES
from Crypto.Protocol.KDF import PBKDF2


def decode(encrypted: bytes, note_password: str, username: str = 'admin') -> bytes:
    # Preprocess the variables
    iv, note = encrypted.split(b'.')
    iv, note = unhexlify(iv), unhexlify(note)
    username = username.encode()

    # Decrypt the note
    key = PBKDF2(note_password, username, dkLen=16, count=1000000)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    content = cipher.decrypt(note)
    return content


# Set the variables
user = 'admin'
password = 'dq1shHUb'
encrypted_note = b"950902d52cf09d9c25bc476361119bfd.f0a6f3dfa5163aff51b4bd3123bb20db907a4532b58a9adf331948c787b14883ce87777b9b367a78b95a34ab9c771171696aca7087ed8da47f3496b6d7b55bea"  # noqa: E501

if __name__ == "__main__":
    result = decode(encrypted=encrypted_note, note_password=password, username=user)
    print(result)
