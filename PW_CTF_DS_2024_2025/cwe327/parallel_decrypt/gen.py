# Simplistic file generator for testing purposes
if __name__ == '__main__':
    file_name = 'in.txt'

    f = open(file_name, 'wb')
    f.write(b"alamakot" * 10000000)
    f.close()
    print(f"File '{file_name}' created!")
