import string

ALPHABET = string.ascii_lowercase + string.digits


def encrypt(password, text):
    message = "".join([c.lower() if c.isalnum() else "" for c in text])
    plaintext = [ALPHABET.find(c.lower()) for c in message]
    keystream = [ALPHABET.find(c.lower()) for c in password]
    n = len(plaintext)
    m = len(keystream)
    ciphertext = [(plaintext[i] + keystream[i % m]) % len(ALPHABET) for i in range(n)]
    return "".join([ALPHABET[c] for c in ciphertext])


def decrypt(password, text):
    message = "".join([c.lower() if c.isalnum() else "" for c in text])
    ciphertxt = [ALPHABET.find(c.lower()) for c in message]
    keystream = [ALPHABET.find(c.lower()) for c in password]
    n = len(ciphertxt)
    m = len(keystream)
    plaintext = [(ciphertxt[i] - keystream[i % m]) % len(ALPHABET) for i in range(n)]
    return "".join([ALPHABET[c] for c in plaintext])


flag = "fa5ef1a9"  # sample flag
text = "hello world"  # sample text
key1 = "ab"  # sample key #1
key2 = "def"  # sample key #2
key3 = "uvxyz"  # sample key #3
text0 = text + ("pw" + "open" + flag + "close") + text
text1 = encrypt(key1, text0)
text2 = encrypt(key2, text1)
text3 = encrypt(key3, text2)
ciphertext = text3

print(decrypt(key1, decrypt(key2, decrypt(key3, ciphertext))))
