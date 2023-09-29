#!/usr/bin/python3

"""
1. Python script takes your GitHub credentials (username and password)
    and uses the GitHub API to display your id
2. Must use Basic Authentication with a personal access token as password
    to access to your information (only read:user permission is needed)
3. First argument will be your username
4. Second argument will be your password (personal access token as password)
5. Must use the package requests and sys
6. Only allowed to import requests and sys packages
7. No need to check arguments passed to the script (number or type)
"""

import requests
import sys

# check if username and password passed to command line argument
if len(sys.argv) != 3:
    print('Usage: ./10-my_github.py <username> <password>')
    sys.exit(1)

# get username and password from command line argument
username = sys.argv[1]
password = sys.argv[2]

# set url
url = 'https://api.github.com/user'
username = sys.argv[1]
password = sys.argv[2]

# Set up authentication
auth = (username, password)

try:
    response = requests.get(url, auth=auth)
    json_data = response.json()
    print(json_data['id'])
except Exception as e:
    print("None")
