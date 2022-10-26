#!/usr/bin/python3
"""
This module contains the read_file funtion
"""


def read_file(filename=""):
    """ Reads the file"""
    with open(filename, 'r', encoding='UTF8') as f:
        print(f.read(), end="")
