import requests
import json
class SnovBaseRequestBody():
    def __init__(self) -> None:
        url = "http://192.168.1.10:8000/snov/get_cookies"
        cookies = requests.get(url)
        cookies  = json.loads(cookies.text)
        self.cookies.update(cookies)
        url  = "http://192.168.1.10:8000/snov/get_header"
        headers =  json.loads(requests.get(url).text)
        self.headers.update(headers)
        
        