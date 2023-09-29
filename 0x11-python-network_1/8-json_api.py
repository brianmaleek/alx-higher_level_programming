#!/usr/bin/python3

"""
1. Python script takes in a letter, sends a POST request to
    http://0.0.0.0:5000/search_user with the letter as a parameter.
2. The letter must be sent in the variable q
3. If no argument is given, set q=""
4. The response body is properly JSON formatted and not empty,
    display the id and name like this: [<id>] <name>
5. Otherwise:
        Display Not a valid JSON if the JSON is invalid
        Display No result if the JSON is empty
6. Must use the package requests and sys
7. Only import requests and sys packages
"""

import requests
import sys

# check if letter passed to command line argument
if len(sys.argv) != 2:
    q = ""
else:
    q = sys.argv[1]

# set url
url = "http://0.0.0.0:5000/search_user"
data = {'q': q}

try:
    response = requests.post(url, data=data)
    json_data = response.json()

    if json_data:
        print("[{}] {}".format(json_data['id'], json_data['name']))
    else:
        print("No result")
except Exception as e:
    print("Not a valid JSON")
