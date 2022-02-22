import json
import jsonpath
import requests
def data1(datatypes):
  url = datatypes
  data1 = requests.get(url)
  data2 = json.loads(data1.text)
  #print(data2)
  pages = jsonpath.jsonpath(data2, "total")
  print(pages[0])
  assert pages[0] == 12
data_url = "https://reqres.in/api/users?page=2"
data1(data_url)
