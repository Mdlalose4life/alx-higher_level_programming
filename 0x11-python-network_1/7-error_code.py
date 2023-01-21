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
    status = requests.status_code
    if status_code <= 400:
    	print("Error code:")
    
