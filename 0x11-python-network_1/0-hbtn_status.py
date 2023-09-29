#!/usr/bin/python3

"""
A script that fetches https://intranet.hbtn.io/status
"""

import urllib.request

if __name__ == '__main__':
    url = "https://alx-intranet.hbtn.io/status"
    with urllib.request.urlopen(url) as response:
        data_content = response.read()
        data_content_decode = data_content.decode("utf-8")
        data_content_type = type(data_content)
        print("Body response:")
        print("\t- type: {}".format(data_content_type))
        print("\t- content: {}".format(data_content))
        print("\t- utf8 content: {}".format(data_content_decode))
