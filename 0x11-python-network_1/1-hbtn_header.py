#!/usr/bin/python3
"""
Python script that
1. takes in a URL 
2. sends a request to the URL
3. displays the value of the X-Request-Id variable found
in the header of the response.
"""
from urllib import request
import sys

if __name__ == "__main__":
    with request.urlopen(sys.argv[1]) as reponse:
    	print(response.getheader("X-Request-Id"))
