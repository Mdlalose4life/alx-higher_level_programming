#!/usr/bin/python3
"""
A module that contains the class BaseGeometry
"""


class BaseGeometry:
    """A class with public attribute area"""
    def area(self):
        """raises an exception when called"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if type(value) is not int:
            raise TypeError("{:s} must be an integer")
        if value <= 0:
            raise ValueError("{:s} must be greater than 0")

class Rectangle(BaseGeometry):
    """This class represent a rectangle"""
    def __init__(self, width, height):
        """Contruct a class"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("hight", height)
        self.__hight = height
    def area(self):
        """returns the area of the rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """returns the string representation of the rectangle"""
        return "width: {:d}, height: {:d}".format(self.__width, self.__hight)

