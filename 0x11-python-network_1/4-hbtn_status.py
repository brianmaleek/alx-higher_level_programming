#!/usr/bin/python3

"""
1. Python script fetches https://alx-intranet.hbtn.io/status
2. Must use the package requests
3. Only import requests package
4. Body response must be display like the following example
    (tabulation before -)
"""

import requests

if __name__ == "__main__":
    url = 'https://intranet.hbtn.io/status'

    try:
        # send request to URL
        response = requests.get(url)
        # display body response
        print('Body response:')
        print('\t- type: {}'.format(type(response.text)))
        print('\t- content: {}'.format(response.text))
    except requests.exceptions.HTTPError as e:
        # Handle HTTPError errors
        print('Error code: {}'.format(e.code))
