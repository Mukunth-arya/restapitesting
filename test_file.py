import jsonpath
import json
import requests
url  = "https://reqres.in/api/users/2"
def test_files():
    data1 = open("E:\\myfile\\myfiles2.json", 'r')
    data2 = data1.read()
    data3 = json.loads(data2)

    data4 = requests.put(url, data3)
    assert data4.status_code == 200

    data5 = json.loads(data4.text)
    updated = jsonpath.jsonpath(data5, "updatedAt")
    print(updated[0])


test_files()