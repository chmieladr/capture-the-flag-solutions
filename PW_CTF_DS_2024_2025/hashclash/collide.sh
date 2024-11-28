#!/bin/bash

docker run --rm -it -v $PWD:/work -w /work -u $UID:$GID brimstone/fastcoll --prefixfile prefix -o msg1.bin msg2.bin
cat msg1.bin suffix > safe.py
cat msg2.bin suffix > malicious.py