from sys import argv, stderr

from executors import encrypt_ecb_parallel, decrypt_ecb_parallel, \
    encrypt_cbc, decrypt_cbc_parallel, process_ctr_parallel
from utils import usage_message, iv_message, nonce_message

# Adjust to your system/needs
num_processes = 16

if __name__ == '__main__':
    if len(argv) != 5 and len(argv) != 6:
        print(usage_message, file=stderr)
        exit(1)

    # Determine input and output files
    input_file = argv[1]
    output_file = argv[2]

    try:
        input_text = open(input_file, 'rb').read()
        key = argv[3].encode()

        if argv[4] == '1':
            result = encrypt_ecb_parallel(key, input_text, num_processes=num_processes)
        elif argv[4] == '2':
            result = decrypt_ecb_parallel(key, input_text, num_processes=num_processes)
        elif argv[4] == '3':
            if len(argv) != 6:
                print(iv_message, file=stderr)
                exit(2)
            iv = argv[5]
            result = encrypt_cbc(key, input_text, iv)
        elif argv[4] == '4':
            if len(argv) != 6:
                print(iv_message, file=stderr)
                exit(2)
            iv = argv[5]
            result = decrypt_cbc_parallel(key, input_text, iv, num_processes=num_processes)
        elif argv[4] == '5':
            if len(argv) != 6:
                print(nonce_message, file=stderr)
                exit(3)
            nonce = argv[5].encode()
            result = process_ctr_parallel(key, input_text, nonce, num_processes=num_processes)
        else:
            print('Invalid mode!', file=stderr)
            exit(4)
    except (OSError, FileNotFoundError):
        print('File operation error!', file=stderr)
        exit(5)
    except (OverflowError, ValueError):
        print('Invalid key, IV or nonce!', file=stderr)
        exit(6)
    except TypeError as e:
        print(e, file=stderr)
        exit(7)

    output = open(output_file, 'wb')
    output.write(result)
    output.close()
    print(f'Encrypted data saved to {output_file}!')
