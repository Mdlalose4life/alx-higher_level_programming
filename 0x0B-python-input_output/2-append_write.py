#!/usr/bin/python3
"""
This module contains a append_file funtion
"""


def append_write(filename="", text=""):
    """Appends the text to the end of the filename then
    Retuns the number of characters appended to the end of the file"""
    with open(filename, 'a', encoding='UTF8') as f:
        return f.write(text)
