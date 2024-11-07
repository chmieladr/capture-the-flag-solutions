# Encoded message
**_Reverse Engineering_**
Difficulty: Medium

### 1. Open the provided program in Binary Ninja
After that we want to look for the actual code of the program. Here are my findings:
```c
080491d6  void* encode(char* arg1)
080491ee      size_t eax = strlen(arg1)
08049203      void* result = malloc(bytes: eax + 1)
08049203      
0804923e      for (int32_t i = 0; i u< eax; i += 1)
08049232          *(result + i) = arg1[eax - i - 1]
08049232      
08049248      *(eax + result) = 0
08049286      int16_t eax_24 = ((eax u% 0xc * 0x2a2 u/ 0x11d).w + 0x113) & 0x1f
08049286      
08049321      for (int32_t i_1 = 0; i_1 u< eax; i_1 += 1)
080492a0          int16_t var_16_1
080492a0          
080492a0          if ((i_1 & 1) != 0)
080492ce              var_16_1 = zx.w(*(result + i_1)) - eax_24
080492a0          else
080492b5              var_16_1 = zx.w(*(result + i_1)) + eax_24
080492b5          
080492df          if (var_16_1 s< 0 || var_16_1 s> 0xff)
080492fa              printf(format: &data_804a008, sx.d(*(result + i_1)))
08049302              return nullptr
08049302          
08049315          *(result + i_1) = var_16_1.b
08049315      
08049327      return result


0804932f  int32_t main()
08049336      void* const __return_addr_1 = __return_addr
0804933d      void* var_10 = &arg_4
08049360      FILE* fp = fopen(filename: "outputMessage", mode: &data_804a038)
08049360      
0804936f      if (fp == 0)
08049385          fwrite(buf: &data_804a04c, size: 1, count: 0x30, fp: *stderr)
0804938d          return 1
0804938d      
080493b9      void var_21e
080493b9      
080493b9      for (int32_t i = 0; i s<= 0x201; i += 1)
080493ab          *(i + &var_21e) = 0
080493ab      
080493c5      printf(format: &data_804a080)
080493e5      fgets(buf: &var_21e, n: 0x202, fp: *stdin)
08049406      *(&var_21e + strcspn(&var_21e, &data_804a0a3)) = 0
08049418      puts(str: &var_21e)
0804942a      void* buf = encode(&var_21e)
0804942a      
08049439      if (buf == 0)
0804943b          return 1
0804943b      
08049460      fwrite(buf, size: strlen(&var_21e) + 1, count: 1, fp)
08049472      puts(str: &data_804a0a8)
0804947a      return 0
```

### 2. Understand how the program works
It's really helpful to rename the variables to something that will give us a clear idea of what the program does. You can find the result in `encoder.c` file!

However if you don't want to look at that file yet, here's a step-by-step explanation of the process:
* reverse the string
* calculate a transformation value based on the length
    * formula: `length % 12 * 0x2a2 / 0x11d + 0x113 & 0x1f`
* add this value to characters on even indexes
* subtract this value from characters on odd indexes
* encoding fails if any final value isn't within ASCII characters range

### 3. Prepare another program that reverts this process
Then you can use it to simply decode the provided message that is indeed the flag. You can find my decoder in `decoder.c` file!

> It is important to use file operations instead of copying their context into standard input as they might contain unprintable characters after encoding that likely won't get copied.

### 4. Result
Flag: `EE_CTF{J3dN4_RoB0OTk4_mI3Si4C_W0oDKA_150419}`