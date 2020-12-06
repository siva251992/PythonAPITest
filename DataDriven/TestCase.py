import requests
import jsonpath
import json
import openpyxl
from DataDriven import Library

obj = Library.Common('C:\\Users\\esivxxx\\Desktop\\APIAutomation\\StudentData.xlsx','Sheet1')
col =obj.fetch_column_count()
row = obj.fetch_row_count()
keylist = obj.fetch_key_names()

def test_add_multiple_students():
    API_Url = 'http://thetestingworldapi.com/api/studentsDetails'
    f = open('C:\\Users\\esivxxx\\Desktop\\APIAutomation\\AddNewStudent.json', 'r')
    json_req = json.loads(f.read())
    #excelcode
    obj = Library.Common('C:\\Users\\esivxxx\\Desktop\\APIAutomation\\StudentData.xlsx', 'Sheet1')
    col = obj.fetch_column_count()
    row = obj.fetch_row_count()
    keylist = obj.fetch_key_names()

    for i in range(2,row+1):
        updated_json_request =  obj.update_request_with_data(i,json_req,keylist)
        response = requests.post(API_Url,updated_json_request)
        print(response)


