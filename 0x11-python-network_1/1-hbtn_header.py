#!/usr/bin/python3
"""Takes in a URL, sends a request to the URL and displays the value of the"""

import sys
import urllib.request

if __name__ == "__main__":
    # Get the URL argument from the command line
    url = sys.argv[1]

    # Open the URL and get the response object
    with urllib.request.urlopen(url) as response:
        # Get the value of the X-Request-Id variable from the header
        x_request_id = response.get_header("X-Request-Id")

    # Display the value
    print(x_request_id)
