#!/usr/bin/python3
"""
script that fetches https://alx-intranet.hbtn.io/status
"""

import requests


if __name__ == "__main__":
    req = request.get('ttps://alx-intranet.hbtn.io/status')
    print('Body response:')
    print('\t -type: {}'.format(type(req)))
    print('\t -content: {}'.format(req))
    
