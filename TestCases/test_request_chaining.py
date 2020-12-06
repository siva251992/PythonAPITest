import json
import requests
import jsonpath


def test_add_student_data():
    global id_re
    API_Url='http://thetestingworldapi.com/api/studentsDetails'
    f=open('C:\\Users\\esivxxx\\Desktop\\APIAutomation\\ReqestJson.json','r')
    data=f.read()
    json_req=json.loads(data)
    response=requests.post(API_Url,json_req)
    id_re = jsonpath.jsonpath(response.json(),'id')
    print(id_re[0])

def test_get_student_data():
    id= test_add_student_data()
    API_Url = 'http://thetestingworldapi.com/api/studentsDetails/'+str(id_re[0])
    #print(API_Url)
    response = requests.get(API_Url)
    print(response.text)
    print(id_re[0])
