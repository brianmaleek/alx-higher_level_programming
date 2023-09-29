#!/usr/bin/python3

"""
1. Python script takes in a URL, sends a request to the URL and displays
    the value of the variable X-Request-Id in the response header
2. Use the packages requests and sys
3. Only import requests and sys packages
4. Value of this variable should be different for each request
5. No need to check script arguments (number and type)
"""


import requests
import sys

# check url passed to command line argument
if len(sys.argv) != 2:
    print('Usage: ./5-hbtn_header.py <URL>')
    sys.exit(1)

# get url from command line argument
url = sys.argv[1]

try:
    response = requests.get(url)
    x_request_id = response.headers.get('X-Request-Id')
    if x_request_id:
        print(x_request_id)
    else:
        print('None')
except requests.RequestException as e:
    print('Error sending request: {}'.format(e))
