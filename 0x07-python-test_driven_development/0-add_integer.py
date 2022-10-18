#!/usr/bin/python3
"""
This is 0-add_integer.py Module.
This Module provides a function that adds two intergers or floats.
"""


def add_integer(a, b=98):
    """All digits must be intergers or floats"""
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")
    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)
    """Returns the addition of two digits."""
    sum = a + b
    return sum
