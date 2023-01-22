#!/usr/bin/python3
"""
script that 
1. takes your GitHub credentials (username and password) 
2. uses the GitHub API to display your id
"""

import requests
import sys

if __name__ == "__main__":
    resp = requests.get("https://api.gihub.com/user", (sys.argv[1],sys.argv[2]))
    try:
        print(resp.json().get("id"))
    except ValueError:
        print("Not a valid JSON")
