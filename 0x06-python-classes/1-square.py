#!/usr/bin/python3
"""Defines a class Square"""


class Square:
    """Represent a square
    Attribute:
        __size(int): size of a side of the square
    """
    def __init__(self, size):
        """Initializes a square

        Args:
            size (int): size of a side of the square

            Return: None
        """
        self.__size = size
