#!/usr/bin/python3

"""
1. Script takes in a URL and an email, sends a POST request to the
    passed URL with the email as a parameter, and displays the
    body of the response (decoded in utf-8)
2. Email must be sent in the email variable
3. Must use the packages urllib and sys
4. Not allowed to import packages other than urllib and sys
5. No need to check arguments passed to the script (number or type)
6. Must use the with statement
"""

from urllib import request, parse
import sys

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print('Usage: ./2-post_email.py <URL> <email>')
        sys.exit(1)

    url = sys.argv[1]
    email = sys.argv[2]

    # prepare data to send as POST request
    data = parse.urlencode({'email': email}).encode('utf-8')

    try:
        # send POST request to URL with data
        with request.urlopen(url, data) as response:
            body = response.read()
            body_decode = body.decode('utf-8')
            print(body_decode)
    except request.HTTPError as e:
        # Handle HTTPError errors
        print('Error code: {}'.format(e.code))
    except Exception as e:
        # Handle all other errors
        print("An error occurred: {}".format(e))
