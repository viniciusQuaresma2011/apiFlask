
from urllib import request, response
import requests
from flask import jsonify

BASE = "http://127.0.0.1:5000/"

headers = {'accept': 'application/json'}

payload = {"name": "tiziu", "views": 4, "likes": 10}


data = [{"name": "tiziu1", "views": 5, "likes": 11},
        {"name": "tiziu2", "views": 6, "likes": 12},
        {"name": "tiziu3", "views": 9, "likes": 15}]



for i in enumerate(data):
    response = requests.put(BASE + 'video/' + str(i), data=[i])
    print(response)

input()

# response = requests.delete(BASE + 'video/0')
# print(response.json())


# response = requests.get(BASE + "video/6")
# print(response.json())








