import json
import jsonpath
import requests

def data():
    url = "https://reqres.in/api/users/2"
    data2 = requests.delete(url)
    print(data2.status_code)
    assert data2.status_code == 200
data()