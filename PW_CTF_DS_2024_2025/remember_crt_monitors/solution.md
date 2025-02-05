# Remember CRT Monitors?
Difficulty: Easy

### 1. Analyze all the given files
The provided files are:
- `decrypt` - program used to decrypt the messages
- `encrypt` - program used to encrypt the messages
- `messages` - file containing the encrypted messages and not only that...
- `recepients` - more compressed form of the `messages` file (not very useful)
- `server.py` - Python script used to encrypt the messages using the programs mentioned above

### 2. (Optional) Decompiling the programs
To discover how exactly this encryption works, you can use Binary Ninja (or Ghidra) to decompile the provided programs
(as it is mentioned, these are 64-bit Linux binaries).
Then we can use the AI to rewrite the code in a more readable form. 

> **Note!**
> Although I have personally done this step (you can find my results in `decrypt.c` and `encrypt.c` files),
> I believe this process is fully optional.

### 3. Analyse `messages` file and the title
The `messages` file was generated in the following form:
```
[*] kid = 0
[*] mod = 125283690561560721600621315130029082980656301198912597163826105946048136616941371375415986346147795139082742022679938433213865869167221360814722295867890703297375391326146413963337123755247069179570730590532218377855190583535801483062716397839316883286454624803071085988249678304170349844775327972117506485347
[*] enc = 89459713939054533398975824766383942123769236871035323940592102852839177026646388086819228869035253595800195192916377637906802011379982306829929149193464248521865503093279761097171877378524236611307678507862943708110572722670040091233384875618752189205503638845667686043325222975996828532772445005826155376527

[*] kid = 1
[*] mod = 93185628086335302912603419869836825751474922390365552421325923903905427496885384318268120611790862087918920271762916958730142615582002185545912452342386889002361201162124182226275162738635638929805074019485588166125948605184533002406587521106407385984014851707408817271973194578059364425545445412492795334621
[*] enc = 28546060327398231875091217156427183663961858241893263472820734321938339416305700699074276084639316633858671563136275670791449356299909937197324095723191671406215791810016312943649633122766787819982994135658669721279201205211925307207094801807649860355751063222493831585419380126875974854509997126028459890781

...
```

Now let's explain every variable in here:
- `kid` - the ID of the message
- `mod` - the modulus used in the encryption
- `enc` - the encrypted message

Note that all the plaintext is always the same, along with the exponent used in the encryption.
The only thing that changes is the modulus.

Other than that, the title mentions CRT monitors.
This is a hint that the encryption method used in this task is the **Chinese Remainder Theorem**.
There's actually a known vulnerability in CRT when the same exponent is used for all the messages.
This is the case here.

### 4. Exploiting same `e` with different moduli
If the same plaintext \( m \) is encrypted using the same \( e \) but different moduli \( n_1, n_2, \dots, n_k \), we get:
\[
c_1 = m^e \mod n_1, \quad c_2 = m^e \mod n_2, \dots
\]

This creates a system of modular equations.
Then combine the ciphertexts \( c_1, c_2, \dots \)
to compute \( M = m^e \mod N \), where \( N = n_1 \cdot n_2 \cdot \dots \cdot n_k \).
\( M = m^e \) can then be decrypted by finding the \( e \)-th root of \( M \) using `iroot`.

This is possible because CRT reconstructs \( m^e \) in full, bypassing modulus constraints, allowing recovery of \( m \).

### 5. Iterating through different exponent values
The only thing left is to iterate through different exponent values
and check if the decrypted text for given `e` starts with `PW{`.
If it does, we have found the flag.

### 6. Result
e: `17` \
Raw bytes: `b'PW{0_oCRT4da6fc8e92286b0e}'` \
Flag: `PW{0_oCRT4da6fc8e92286b0e}`