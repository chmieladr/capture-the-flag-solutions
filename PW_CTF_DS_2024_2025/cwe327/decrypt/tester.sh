#!/bin/bash
# $1 - file name with no .bmp extension

# Cleans files from previous execution
rm ./*crypted.bmp 2>/dev/null
rm ./*crypted_full.bmp 2>/dev/null

# Executes python script
python3 main.py "$1"
# kate "$1".bmp "$1"_CBC_decrypted_full.bmp "$1"_ECB_decrypted_full.bmp &  # debugging purposes

# Opens files with gwenview
gwenview "$1".bmp 2>/dev/null
gwenview "$1"_CBC_decrypted.bmp 2>/dev/null
gwenview "$1"_ECB_decrypted.bmp 2>/dev/null
gwenview "$1"_CBC_decrypted_full.bmp 2>/dev/null
gwenview "$1"_ECB_decrypted_full.bmp 2>/dev/null