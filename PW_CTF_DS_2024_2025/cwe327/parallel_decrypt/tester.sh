#!/bin/bash
# Tester script for the parallel encryption program
# First encrypts the input file using the specified mode
# Then tries to decrypt it using the same mode
# Usage: ./tester.sh [mode]

# Variables
in="in.txt"
tmp="in2.txt"
out="out.txt"
key="theballisbig1234"  # must be 16 characters
iv="cocojumbo123456@"  # must be 16 characters
nonce="chmieladr" # should be kept equal or less than 12 characters

if [ -z "$1" ]; then
  echo "Usage: ./tester.sh [mode]"
  echo "Available modes: ECB, CBC, CTR"
  exit 1
fi

# Check if the input file exists
if [ ! -f $in ]; then
  read -r -p "Input file not found! Do you want to generate it? (y/n): " ans
  if [ "$ans" == "y" ]; then
    python3 gen.py
  else
    echo "Input file not found! (generation skipped...)"
    exit 2
  fi
fi

# Main execution
if [ "$1" == "ECB" ]; then
  python3 main.py $in $tmp $key 1
  python3 main.py $tmp $out $key 2
elif [ "$1" == "CBC" ]; then
  python3 main.py $in $tmp $key 3 $iv
  python3 main.py $tmp $out $key 4 $iv
elif [ "$1" == "CTR" ]; then
  python3 main.py $in $tmp $key 5 $nonce
  python3 main.py $tmp $out $key 5 $nonce
else
  python3 main.py
  exit 3
fi

# shellcheck disable=SC2181
if [ $? -ne 0 ]; then
  echo "Error occurred during encryption/decryption!"
  exit 4
fi

# Compare the initial file with the one that was encrypted and decrypted
if cmp -s $in $out; then
    echo "$1 mode works correctly!"
    rm $tmp $out # clean up if works correctly
else
    echo "$1 mode doesn't work correctly!"
    if [ "$(stat -c%s "$in")" -le 256 ] && [ "$(stat -c%s "$out")" -le 256 ]; then
        echo "Input file:"
        xxd $in
        echo "Output file:"
        xxd $out
    fi
fi