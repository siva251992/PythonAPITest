import requests
import json
import jsonpath

url = "https://reqres.in/api/users/2"

response = requests.delete(url)
print(response.status_code)

try:
    assert response.status_code == 204, 'Not Deleted'
    print('Deleted Successfully')
except AssertionError as msg:
    print(msg)
