import requests
import json
import jsonpath
import pytest

def test_Add_new_data():
    API_Url='http://thetestingworldapi.com/api/studentsDetails'
    f = open('C:\\Users\\esivxxx\\Desktop\\APIAutomation\\ReqestJson.json', 'r')
    json_req = json.loads(f.read())
    response = requests.post(API_Url, json_req)
    print(response.text)
    id=jsonpath.jsonpath(response.json(),'id')
    print(id[0])

    tech_url ='http://thetestingworldapi.com/api/technicalskills'
    f = open('C:\\Users\\esivxxx\\Desktop\\APIAutomation\\Tech_Details.json', 'r')
    json_req = json.loads(f.read())
    json_req['id'] = int(id[0])
    json_req['std_id'] = id[0]
    response =  requests.post(tech_url,json_req)
    print(response.text)

    add_api_url = 'http://thetestingworldapi.com/api/addresses'
    f = open('C:\\Users\\esivxxx\\Desktop\\APIAutomation\\Add_Details.json', 'r')
    json_req = json.loads(f.read())
    json_req['std_id'] = id[0]
    response = requests.post(add_api_url, json_req)
    print(response.text)
    print(response.status_code)

    final_details='http://thetestingworldapi.com/api/FinalStudentDetails/'+str(id[0])
    response=requests.get(final_details)
    print(response.text)
