#!/usr/bin/python3
"""
Defines a class Rectangle
"""


class Rectangle:
    """Represents the rectangle"""
    def __init__(self, width=0, height=0):
        """Initializes the rectangle"""
        self.height = height
        self.width = width

    @property
    def width(self):
        """gets the width of a ractangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """sets the width of a trigle"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """gets the height of a rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

        def area(self):
            """Returns the area of a Ractangle"""
            return self.__width * self.__height
        
        def perimeter(self):
            """Returns the perimeter of a rectangle"""
            if self.__width == 0 or self.__height == 0:
                return 0
            return (self.__width * 2) + (self.__height * 2)
