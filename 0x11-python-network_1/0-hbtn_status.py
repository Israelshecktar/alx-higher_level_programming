#!/usr/bin/python3
"""Fetches https://alx-intranet.hbtn.io/status"""

import urllib.request

if __name__ == "__main__":
    # Open the URL and read the response
    with urllib.request.urlopen("https://alx-intranet.hbtn.io/status") as response:
        body = response.read()

    # Display the type, content, and utf8 content of the response body
    print("Body response:")
    print("\t- type: {}".format(type(body)))
    print("\t- content: {}".format(body))
    print("\t- utf8 content: {}".format(body.decode("utf-8")))
