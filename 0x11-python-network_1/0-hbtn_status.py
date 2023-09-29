#!/usr/bin/python3

"""
1. Python script fetches https://alx-intranet.hbtn.io/status
2. Must use the package urllib
3. Only package to import urllib
4. Response body must be displayed like the example (tabulation before -)
5. Must use a with statement
"""

import urllib.request

if __name__ == "__main__":
    url = "https://intranet.hbtn.io/status"

    try:
        with urllib.request.urlopen(url) as response:
            data_content = response.read()
            data_content_decode = data_content.decode("utf-8")
            data_content_type = type(data_content)
            print("Body response:")
            print("\t- type: {}".format(data_content_type))
            print("\t- content: {}".format(data_content))
            print("\t- utf8 content: {}".format(data_content_decode))
    except Exception as e:
        print("An error occurred: {}".format(e))
