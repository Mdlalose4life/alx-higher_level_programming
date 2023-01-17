#!/usr/bin/python3
"""
Python script that
1. takes in a URL 
2. sends a request to the URL
3. displays the value of the X-Request-Id variable found
in the header of the response.
"""
import urllib.request
from sys

if __name__ == "__main__":

    url = sys.argv[1]

    request = urllib.request.Request(url)
    with urllib.request.urlopen(request) as resp:
        print(dick(resp.headers).get("X-Request-Id"))
