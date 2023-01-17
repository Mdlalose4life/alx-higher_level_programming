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
    with request.urlopen(sys.argv[1]) as response:
        print(response.getheader("X-Request-Id"))
