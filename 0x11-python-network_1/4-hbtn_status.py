#!/usr/bin/python3

"""
1. Python script fetches https://alx-intranet.hbtn.io/status
2. Must use the package requests
3. Only import requests package
"""

import requests


if __name__ == "__main__":
    url = 'https://alx-intranet.hbtn.io/status'
    # send request to URL
    response = requests.get(url)
    # display body response
    print('Body response:')
    print('\t- type: {}'.format(type(response.text)))
    print('\t- content: {}'.format(response.text))
