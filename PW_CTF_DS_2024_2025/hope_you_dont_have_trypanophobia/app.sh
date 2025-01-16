#!/bin/bash

if [ "$#" -ne 1 ]; then
  echo "Script that launches the app with the specified vulnerability."
  echo "Usage: $0 <xss|sqli>"
  exit 1
fi

if [ "$1" == "xss" ]; then
  cd app_xss || exit 2
  python3 hello.py
elif [ "$1" == "sqli" ]; then
  cd app_sqli || exit 2
  python3 hello.py
else
  echo "Invalid argument!"
  echo "Usage: $0 <xss|sqli>"
  exit 3
fi