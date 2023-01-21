#!/usr/bin/python3
"""
Script that
1. takes in a URL.
2. sends a request to the URL
3. displays the value of the variable X-Request-Id in the response header
"""

import requests
import sys

if __name__ == "__main__":
    resp = requests.get(sys.argv[1])
    print(resp.headers.get("X-Request-Id"))
