#!/usr/bin/python3
"""

"""

import requests
import sys

if __name__ == "__main__":
    resp = requests.get(sys.argv[1])
    print(resp.headers.get("X-Request-Id"))
