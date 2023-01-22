#!/usr/bin/python3
"""
script that
1. takes in a letter.
2. sends a POST request to http://0.0.0.0:5000/search_user with the letter as a parameter.
"""

import requests
import sys

if __name__ == "__main__":
    data = {"q" : sys.argv[1][0] if len(sys.argv) > 1 else ""}
    req = requests.post("http://0.0.0.0:5000/search_user", data=data)
    try:
        q = req.json()
        if not q:
            print("No result")
        else:
            print("([]) {}".format(q.get("id"), q.get("name"))
    except ValueError:
        print("Not a valid JSON")
