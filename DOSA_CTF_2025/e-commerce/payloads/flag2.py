from req import request

url = "https://task1.ctf.sekangur.pl/api/store/order/1"

if __name__ == "__main__":
    code, text = request(url, method="GET")
    print(f"{code} -> {text}")
