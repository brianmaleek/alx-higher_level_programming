#!/usr/bin/python3

"""
1. Python script takes in a URL, sends a request to the URL and displays
    the value of the X-Request-Id variable found in the header of the response.
2. Use the packages urllib and sys
3. Only import urllib and sys packages
4. Value of this variable should be different for each request
5. No need to check arguments passed to the script (number or type)
6. Must use a with statement
"""

import urllib.request
import sys

if __name__ == "__main__":
    # check url passed to command line argument
    if len(sys.argv) != 2:
        print('Usage: ./1-hbtn_header.py <URL>')
        sys.exit(1)

    url = sys.argv[1]

    try:
        with urllib.request.urlopen(url) as response:
            x_request_id = response.headers.get('X-Request-Id')
            if x_request_id:
                print(x_request_id)
            else:
                print('None')
    except urllib.error.HTTPError as e:
        print('Error code: {}'.format(e.code))
    except Exception as e:
        print("An error occurred: {}".format(e))
