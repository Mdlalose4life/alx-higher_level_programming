#!/usr/bin/python3
"""
This modude contains the class BaseGeometry class and subclass Square.
"""


Rectangle = __import__('9-rectangle').Rectangle

class Square(Rectangle):
    """
    This class represents a square.
    """
    def __init__(self, size):
        """Initialize a square sub class"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """Return the area of a square"""
        return self.__size * 2
        
