import requests
from requests.auth import HTTPBasicAuth

payload = {
    'amount':5
}

print(requests.post('https://storeappapi.herokuapp.com/',json=payload, auth = HTTPBasicAuth('Frabian','Frabian')).text)
