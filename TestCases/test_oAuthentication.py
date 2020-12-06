import json
import requests
import jsonpath
import os

def test_oAuth_api():
    token_url='http://thetestingworldapi.com/Token'

    API_URL='http://thetestingworldapi.com/api/StDetails/1104'
    response=requests.get(API_URL)
    print(response.text)

l=os.listdir('C:\\Users\\esivxxx\\Desktop\\Python_Durga')
k=[]
for i in l:
    j=i.replace('.pdf','')
    k.append(j)

#print(k)

for i in range(len(k)):
    print(k[i])






