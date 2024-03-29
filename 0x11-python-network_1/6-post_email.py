#!/usr/bin/python3
"""
script that
1. takes in a URL and an email address.
2. sends a POST request to the passed URL with the email as a parameter.
3. And finally displays the body of the response
"""


import requests
import sys

if __name__ == "__main__":
    url = (sys.argv[1])
    data = {'email': sys.argv[2]}
    res = requests.post(url, data)
    print(res.text)
