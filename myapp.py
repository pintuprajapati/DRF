"""
- 'myapp.py' is a 3rd party application which calls the API
- Front End is sending JSON data to this API and backend (views.py) will check the request hit by FE and then JSON data will be converted to Python Data.

- myapp.py can be anything. Desktop application, android app, webapp anything. Here just for testing purpose we are using this python code file.
- myapp.py is in the same directory as 'manage.py'

"""

import requests
import json

URL = "http://127.0.0.1:8000/api/studentapi/"

################## GET ##################
# Based on ID, we will fetch the specific data of that ID. 
# If ID is not specified then all the data will be fetched
def get_data(id=None):
    data = {}
    if id is not None:
        data = {'id': id}
    json_data = json.dumps(data) # converting python data into JSON data
    r = requests.get(url = URL, data = json_data) # with GET request, JSON data will be submitted to URL
    data = r.json()
    print("➡ data :", data)

# get_data(2) # to test "GET" api, uncomment this one

################## POST ##################
def post_data():
    data = {
        'name': 'Manoj',
        'roll': 101,
        'city': 'Ranchi'
    }
    json_data = json.dumps(data)
    r = requests.post(url = URL, data = json_data)
    data = r.json()
    print("➡ data :", data)

# post_data() # to test "POST" api, uncomment this one

################## UPDATE ##################
def update_data():
    data = {
        'id': 17,
        'name': 'Manoj1',
        'roll': 121,
        'city': 'Gurugram'
    }
    json_data = json.dumps(data)
    r = requests.put(url = URL, data = json_data)
    data = r.json()
    print("➡ data :", data)

update_data() # to test "UPDATE" api, uncomment this one

################## DELETE ##################
def delete_data():
    data = {
        'id': 18,
    }
    json_data = json.dumps(data)
    r = requests.delete(url = URL, data = json_data)
    data = r.json()
    print("➡ data :", data)

# delete_data() # to test "DELETE" api, uncomment this one
