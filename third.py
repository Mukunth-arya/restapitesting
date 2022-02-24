import json
import jsonpath
import requests

url = "https://reqres.in/api/users"

data1 = open("E:\\myfile\\data.json")
data2 = data1.read()
json1 = json.loads(data2)
data3 = requests.post(url, json1)
assert data3.status_code == 201

data4 = json.loads(data3.text)
id = jsonpath.jsonpath(data4,"id")
print(id[0])