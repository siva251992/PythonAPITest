import requests
from requests.auth import HTTPBasicAuth

def test_with_authentication():
    response = requests.get('https://api.github.com/user',auth=HTTPBasicAuth('siva1992','Tcsilp@159'))
    print(response.text)
