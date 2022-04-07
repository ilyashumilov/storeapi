import requests
from requests.auth import HTTPBasicAuth

payload = {
    'amount':5
}

print(requests.post('https://storeapiservice.herokuapp.com/',json=payload, auth = HTTPBasicAuth('Manuel', 'Manuel')).text)
