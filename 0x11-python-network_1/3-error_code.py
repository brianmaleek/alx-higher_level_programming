#!/usr/bin/python3

"""
1. Python script takes in a URL, sends request to the URL and
    displays the body of the response (decoded in utf-8).
2. Manage urllib.error.HTTPError exceptions and print:
    Error code: followed by the HTTP status code
3. Must use the packages urllib and sys
4. Only import urllib and sys packages
5. No need to check arguments passed to the script (number or type)
6. Must use the with statement
"""

from urllib import request, error
import sys

if __name__ == "__main__":
    if len(sys.argv) != 1:
        print('Usage: 3-error_code.py <URL>')
        sys.exit(1)

    url = sys.argv[1]

    try:
        # send request to URL with data
        with request.urlopen(url) as response:
            html_body = response.read()
            decode_html_body = html_body.decode('utf-8')
            print(decode_html_body)
    except error.HTTPError as e:
        # Handle HTTPError errors
        print('Error code: {}'.format(e.code))
    except Exception as e:
        # Handle all other errors
        print("An error occurred: {}".format(e))
