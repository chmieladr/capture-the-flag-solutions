import struct


def create_bmp_header(file_size, width, height, pixel_data_offset):
    # File Header
    file_header = struct.pack(
        "<2sIHHI",  # '<' = little-endian, 2s = 2-byte string, I = unsigned int, H = unsigned short
        b"BM",  # BMP signature
        file_size,
        0,  # unused 1
        0,  # unused 2
        pixel_data_offset
    )

    # DIB Header (BITMAPINFOHEADER)
    dib_header = struct.pack(
        "<IIIHHIIIIII",
        40,  # header size
        width,
        height,
        1,  # planes
        24,  # bits per pixel
        0,  # compression
        0,  # image size (0 = auto when no compression)
        0,  # X pixels per meter (0 = no preference)
        0,  # Y pixels per meter (0 = no preference)
        0,  # colors used (0 = full palette)
        0  # important colors (0 = all important)
    )

    return file_header + dib_header


def create_color_mapping(color_files: dict, block_size: int = 16) -> dict:
    mapping_dict = {}
    for file, rgb in color_files.items():
        with open(file, "rb") as f:
            data = f.read()
            ciphertext_block = data[4 * block_size:5 * block_size]  # skipping the first 4 blocks as they are the header
            mapping_dict[ciphertext_block] = rgb  # assigning the RGB value to the given ciphertext block
    return mapping_dict


def replace_blocks(input_file: str, output_file: str, mapping_dict: dict, block_size: int = 16):
    with open(input_file, "rb") as f:
        data = f.read()

    output_data = bytearray()
    for i in range(0, len(data), block_size):
        block = data[i:i + block_size]
        if block in mapping_dict:
            rgb = mapping_dict[block] # replacing each block with RGB color (converted to bytes)
            rgb_bytes = struct.pack("BBB", *rgb)
            output_data.extend(rgb_bytes * (block_size // 3))  # filling the first 15 bytes
            output_data.extend(rgb_bytes[:block_size % 3])  # and the 16th last byte
        else:
            output_data.extend(block)  # we leave the block unchanged if we can't find the proper mapping

    with open(output_file, "wb") as f:
        f.write(output_data)