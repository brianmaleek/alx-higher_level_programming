#!/usr/bin/python3

"""
1. Python script takes in a URL and an email address, sends a POST
    request to the passed URL with the email as a parameter, and
    finally displays the body of the response.
2. The email must be sent in the variable email
3. Must use the packages requests and sys
4. Only import requests and sys packages
5. No need to error check arguments passed to the script (number or type)
"""


import requests
import sys

# check url passed to command line argument
if len(sys.argv) != 3:
    print('Usage: ./6-post_email.py <URL> <email>')
    sys.exit(1)

# get url from command line argument
url = sys.argv[1]
email = sys.argv[2]

# create payload
payload = {'email': email}

try:
    response = requests.post(url, data=payload)
    print(response.text)
except requests.RequestException as e:
    print('Error sending request: {}'.format(e))
