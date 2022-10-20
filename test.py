from array import array
from http.client import ACCEPTED
from urllib import request, response
import requests
import json
from flask import jsonify

BASE = "http://127.0.0.1:5000/"

headers = {'accept': 'application/json'}
payload = {"name": "tiziu", "views": 4, "likes": 10}


data = [{"name": "tiziu1", "views": 5, "likes": 11},
        {"name": "tiziu2", "views": 6, "likes": 12},
        {"name": "tiziu3", "views": 9, "likes": 15}]

for i in range(data):
    response = requests.put(BASE + 'video/' + str(i), data=[i.])
    print(response.json())

input()

# response = requests.delete(BASE + 'video/0')
# print(response.json())

response = requests.get(BASE + '/video/list')
print(response.json())






