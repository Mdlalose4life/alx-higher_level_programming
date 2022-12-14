#!/usr/bin/python3
"""Defines a class Square"""


class Square:
    """Represent a square
    Attribute:
        __size(int): size of a side of the square
    """
    def __init__(self, size=0):
        """
        Args:
            size (int): size of a side of the square

            Return: None
        """
        if type(size) is not int:
            raise TypeError('size must be an integer')
        else:
            if size < 0:
                raise ValueError('size must be >= 0')
            else:
                self.__size = size
