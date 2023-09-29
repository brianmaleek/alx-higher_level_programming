#!/usr/bin/python3

"""
1. Python script takes in a URL, sends a request to the URL
    and displays the body of the response.
2. If the HTTP status code is greater than or equal to 400,
    print: Error code: followed by the value of the HTTP status code
3. Must use the packages requests and sys
4. Only import requests and sys packages
5. No need to check arguments passed to the script (number or type)
"""

import requests
import sys

# check url passed to command line argument
if len(sys.argv) != 2:
    print('Usage: ./7-error_code.py <URL>')
    sys.exit(1)

# get url from command line argument
url = sys.argv[1]

try:
    # send request to url
    response = requests.get(url)

    # raise error if bad status code greater than or equal to 400
    if response.status_code >= 400:
        print('Error code: {}'.format(response.status_code))
    else:
        print(response.text)

# print other errors
except Exception as e:
    print('Error: {}'.format(e))
