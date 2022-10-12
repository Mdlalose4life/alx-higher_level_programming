#!/usr/bin/python3
"""Defines a class Square"""


class Square:
    """Represents a square


    Attribute:
        __size(int): size of a side of the square
    """
    def __init__(self, size=0):
        """initializes the square
        Args:
            size (int): size of a side of the square

            Return:
            	None
        """
        if type(size) is not int:
            raise TypeError('size must be an integer')
        else:
            if size < 0:
                raise ValueError('size must be >= 0')
            else:
                self.__size = size

        def area(self):
            """Calulates the square's area

            returns:
                The are of a square
            """
            return (self.__size) ** 2
