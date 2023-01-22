#!/usr/bin/python3
"""
Python script that
1. takes in a URL.
2. sends a request to the URL
3. displays the body of the response.
"""

import requests
import sys

if __name__ == "__main__":
    response = requests.post(sys.argv[0])
    status = requests.status_codes
    if status > 400:
        print("Error code: ")
    else:
        print(response.text)
