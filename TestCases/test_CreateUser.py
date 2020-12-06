import requests
import json
import jsonpath
import pytest

# Api Url
url = "https://reqres.in/api/users"
a = 10


@pytest.fixture()
def start_exec():
    global file
    file = open('C:\\Users\\esivxxx\\Desktop\\Create.json', 'r')
    yield
    file.close()

@pytest.mark.smoke
def test_create_new_user1(start_exec):
    # reading the content from file(String Format)
    json_input = file.read()
    # Typecast to Json format
    requests_json = json.loads(json_input)
    print(requests_json)
    # Make post request with Json I/P
    response = requests.post(url, requests_json)
    print(response.status_code)
    print(response.content)
    # validating response code
    assert response.status_code == 201, "User created"
    print(response.headers.get('Content-Type'))
    # Typecast response to JsonFormat
    response_json = json.loads(response.text)
    # Pick id using jsonpath
    id = jsonpath.jsonpath(response_json, 'id')
    print(id[0])

@pytest.mark.sanity
def test_create_new_user2(start_exec):
    # reading the content from file(String Format)
    json_input = file.read()
    # Typecast to Json format
    requests_json = json.loads(json_input)
    print(requests_json)
    # Make post request with Json I/P
    response = requests.post(url, requests_json)
    print(response.status_code)
    print(response.content)
    # validating response code
    assert response.status_code == 201, "User created"
    print(response.headers.get('Content-Type'))
    # Typecast response to JsonFormat
    response_json = json.loads(response.text)
    # Pick id using jsonpath
    id = jsonpath.jsonpath(response_json, 'id')
    print(id[0])

