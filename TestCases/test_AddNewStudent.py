import requests
import jsonpath
import json
import pytest

def test_add_student_data():
    API_Url='http://thetestingworldapi.com/api/studentsDetails'
    f=open('C:\\Users\\esivxxx\\Desktop\\APIAutomation\\ReqestJson.json','r')
    data=f.read()
    json_req=json.loads(data)
    response=requests.post(API_Url,json_req)
    print(response.json()['id'])
    #return response.json()['id']

def test_get_student_data():
    id= test_add_student_data()
    API_Url = 'http://thetestingworldapi.com/api/studentsDetails/80420'
    #print(API_Url)
    response = requests.get(API_Url)
    json_response = response.json()
    print(json_response['data']['id'])
    id_res=jsonpath.jsonpath(json_response,'data.id')
    assert id_res[0] == 80420

def test_update_student_data():
    id = test_add_student_data()
    API_Url = 'http://thetestingworldapi.com/api/studentsDetails/80420'
    #print(API_Url)
    f = open('C:\\Users\\esivxxx\\Desktop\\APIAutomation\\ReqestJson.json', 'r')
    json_req = json.loads(f.read())
    json_req['first_name']='Hello'
    print(json_req)
    response=requests.put(API_Url,json_req)
    print(response.status_code)
    print(response.text)

def test_delete_student_data():
    API_Url = 'http://thetestingworldapi.com/api/studentsDetails/80420'
    response=requests.delete(API_Url)
    print(response.status_code)


