import re
from sympy.ntheory.modular import crt
from gmpy2 import iroot
from Crypto.Util.number import long_to_bytes


common_exponent = 65537  # commonly used exponent


def extract_mod_and_enc(file_path):
    mod_list = []
    enc_list = []

    # Regexes to match 'mod' and 'enc' values
    mod_pattern = re.compile(r"\[\*] mod = (\d+)")
    enc_pattern = re.compile(r"\[\*] enc = (\d+)")

    with open(file_path, 'r') as file:
        for line in file:
            mod_match = mod_pattern.search(line)
            enc_match = enc_pattern.search(line)
            if mod_match:
                mod_list.append(int(mod_match.group(1)))
            if enc_match:
                enc_list.append(int(enc_match.group(1)))

    return mod_list, enc_list


if __name__ == "__main__":
    moduli, ciphers = extract_mod_and_enc("messages")  # retrieving the data from provided file

    for e in range(1, common_exponent):
        M, _ = crt(moduli, ciphers)  # combine ciphertexts using CRT
        plaintext_root, exact = iroot(M, e)  # recovering M based on e-th root

        if plaintext_root == 1:
            print(f"The plaintext root for current e = {e} equals 1, therefore CRT has failed.")
            break

        plaintext = long_to_bytes(plaintext_root)  # looking for flag
        if plaintext.startswith(b"PW{"):
            print(f"e = {e} -> Flag: {plaintext}")
            break
