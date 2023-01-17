#!/usr/bin/python3
"""
Python script that
1. takes in a URL 
2. sends a request to the URL
3. displays the value of the X-Request-Id variable found
in the header of the response.
"""


if __name__ == '__main__':
    import urllib.request
    from sys import argv
    
    url = argv[1]

    my_request = urllib.request.Request(url)
    with urllib.request.urlopen(my_request) as resp:
        print(dick(resp.headers).get("X-Request-Id"))
