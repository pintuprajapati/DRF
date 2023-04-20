# 3rd party application which calls the API

import requests
import json

URL = "http://127.0.0.1:8000/api/stucreate/"

data = {
    'id': 8,
    'name': 'Sonam',
    'roll': 101,
    'city': 'Ranchi'
}

json_data = json.dumps(data) # converting python data into JSON data
print("➡ json_data :", json_data) # {"id": 4, "name": "Sonam", "roll": 101, "city": "Ranchi"}

r = requests.post(url = URL, data=json_data) # with POST request, JSON data will be submitted to URL

data = r.json()
print("➡ data :", data) # output: {'msg': 'Data Created'}