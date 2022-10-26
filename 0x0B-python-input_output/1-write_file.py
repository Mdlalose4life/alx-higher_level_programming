#!/usr/bin/python3
"""
This module contains a write_file funtion
"""


def write_file(filename="", text=""):
    """Writes text to file name then 
    retuns the number of characters writen"""
    with open(filename, 'w', encoding='UTF8') as f:
        return f.write(text)
