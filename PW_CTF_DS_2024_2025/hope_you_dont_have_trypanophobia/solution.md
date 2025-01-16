# Hope you don't have Trypanophobia
Difficulty: Hard

### 1. Explore the application
Go through all the available pages in the application after authenticating with the provided credentials. We can quickly find out that there's an option to restore your notes from the backup file that's "experimental".

### 2. Check the backup file
We can simply add some notes in the application and then download the backup file. It's a simple JSON file that contains the notes we've added. It looks in the following way:
```json
{
  "317": {
    "encrypted": 0,
    "note": "<p>This is an example note!</p>",
    "title": "Note 1"
  },
  "318": {
    "encrypted": 0,
    "note": "<p>This is another example note!</p>",
    "title": "Note 2"
  },
  "319": {
    "encrypted": 1,
    "note": "2bab16109b9ebd5a72760a19921af9f2.5eb025b0d51acc0664883402340fb80e393f29d1fa876e4c295b45710f7c1c1d",
    "title": "Encrypted Note"
  }
}
```

### 3. Similarities to already used notes
During the "Data Security in IT systems" course, we've already encountered a similar application. We received it in two different versions:
- `app_sqli` subdirectory: contains Flask app vulnerable to SQL injection
- `app_xss` subdirectory: contains Flask app vulnerable to XSS
This way we can locally look for additional vulnerabilities in the application that might work.

### 4. Start uploading payloads using the faulty `restore` feature
All the payloads that I've used have been included in the `payloads.md` file.

### 5. Result
**Username:** `admin`\
**Password:** `dq1shHUb`\
**Encrypted note:** `950902d52cf09d9c25bc476361119bfd.f0a6f3dfa5163aff51b4bd3123bb20db907a4532b58a9adf331948c787b14883ce87777b9b367a78b95a34ab9c771171696aca7087ed8da47f3496b6d7b55bea` \
**Decrypted note:** `b"Scotty didn't know... Take your flag! --> PW{983e5ba50172e631}\x02\x02"` \
**Flag:** `PW{983e5ba50172e631}`

### 6. Second person to solve the challenge
I managed to solve this challenge as the second person which I'm totally satisfied with as I consider this task to be the most difficult one in this entire CTF!