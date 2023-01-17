#!/usr/bin/python3
import urllib.request
"""Pythone script that fetches a URL"""


if __name__ == "__main__":
    with urllib.request.urlopen("https://alx-intranet.hbtn.io/status") as resp:
        html = resp.read()
        print("body responce:")
        print("\t type: {}".format(type(html)))
        print("\t contant {}".format(html))
        print("\t utf-8 content {}".format(html.decode('utf-8')))
