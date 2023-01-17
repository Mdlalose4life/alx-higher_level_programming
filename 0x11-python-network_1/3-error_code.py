#!/usr/bin/python3
"""
script that
1. takes in a URL
2. sends a request to the URL
3. displays the body of the response (decoded in utf-8).
"""

from urllib import request, error
import sys


if __name__ == "__main__":
    try:
        with request.urlopen(sys.argv[1]) as response:
            print(response.read().decode('utf-8'))
    except error.HTTPError as err:
        print("Error code:", err.code)
