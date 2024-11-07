cmake_minimum_required(VERSION 3.10)
project(CTF_EE2024)

set(CMAKE_C_STANDARD 99)

# JIMP Labs
add_executable(jimp_labs
        jimp_labs/saver.c)

# Encoded message
add_executable(encoder
        encoded_message/encoder.c)
add_executable(decoder
        encoded_message/decoder.c)