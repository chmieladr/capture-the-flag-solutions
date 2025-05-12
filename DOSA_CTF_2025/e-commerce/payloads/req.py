import requests

method_mapper = {
    "GET": requests.get,
    "POST": requests.post,
    "PUT": requests.put
}


def request(url: str, method: str, payload: dict | None = None):
    run_http_method = method_mapper[method.upper()]
    response = run_http_method(url, json=payload)
    return response.status_code, response.text
