#!/usr/bin/python3
"""
This is 4-print_square.py module
This module prints the square on screen using # character.
"""


def print_square(size):
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if size > 0:
        for y in range(size):
            for x in range(size):
                print('#', end='')
            print('')
