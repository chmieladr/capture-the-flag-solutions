# COMMENT: random.seed is set based on the flag
import subprocess
import hashlib
import base64
import sys

secret = "# ADBFE529"
# secret = "# " + "".join(random.choices("0123456789ABCDEF", k=8))
whitelist = []
print("[*] Hello on our server!")
print("[*] Your secret is '" + secret + "'")
while True:
    print("[?] Provide a Base64-encoded Python code: ")
    sys.stdout.flush()
    code = base64.b64decode(sys.stdin.buffer.readline())
    print(code)
    digest = hashlib.md5(code).hexdigest()

    if not code.startswith(bytes(secret, "ascii")):
        print("[!] Code has to start with '" + secret + "'")
        continue

    if digest in whitelist:
        print("[ ] Running an already verified code...")
        with open("deadbeef.py", "wb") as f:
            f.write(b"# coding: L1\n")
            f.write(code)
        status = subprocess.run(["python3", "deadbeef.py"], env={})
        print("[*] Done. Exited with return code: " + str(status.returncode))
    else:
        print("[ ] Veryfing if the code is safe to run...")
        with open("deadbeef.py", "wb") as f:
            f.write(b"# coding: L1\n")
            f.write(b"from sys import addaudithook, exit\n")
            f.write(b"def audit(event, args):\n")
            f.write(b"  print('[!] Forbidden event: ' + event)\n")
            f.write(b"  exit(1)\n")
            f.write(b"addaudithook(audit)\n")
            f.write(code)
        status = subprocess.run(["python3", "deadbeef.py"], env={})
        if status.returncode == 0:
            print("[+] Code is safe. Remember the hash digest.")
            whitelist.append(digest)
        else:
            print("[!] Code uses forbidden calls.")
        whitelist.append(digest)
