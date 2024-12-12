from bmp_utils import create_bmp_header, create_color_mapping, replace_blocks


if __name__ == "__main__":
    prefix = "encrypted/"
    suffix = "_RGB_48x20px_ECB_encrypted.bmp"
    color_files = {
        f"{prefix}010101{suffix}": (1, 1, 1),
        f"{prefix}020202{suffix}": (2, 2, 2),
        f"{prefix}030303{suffix}": (3, 3, 3),
        f"{prefix}040404{suffix}": (4, 4, 4),
        f"{prefix}050505{suffix}": (5, 5, 5),
        f"{prefix}FAFAFA{suffix}": (250, 250, 250),
        f"{prefix}FBFBFB{suffix}": (251, 251, 251),
        f"{prefix}FCFCFC{suffix}": (252, 252, 252),
        f"{prefix}FDFDFD{suffix}": (253, 253, 253),
        f"{prefix}FEFEFE{suffix}": (254, 254, 254),
    }

    aes_block_size = 16  # typical AES block size
    mapping = create_color_mapping(color_files, aes_block_size)

    input_file = f"{prefix}barcode_RGB_280x558px_ECB_encrypted.bmp"
    output_file = "result_no_header.bmp"
    replace_blocks(input_file, output_file, mapping, aes_block_size)

    # BMP header information
    file_size = 468768
    width = 280
    height = 558
    image_size = 3 * width * height
    pixel_data_offset = file_size - image_size
    header = create_bmp_header(file_size, width, height, pixel_data_offset)  # creating the BMP header

    with open("result_final.bmp", "wb") as final_file:
        final_file.write(header)
        with open(output_file, "rb") as barcode:
            final_file.write(barcode.read()[54:])
