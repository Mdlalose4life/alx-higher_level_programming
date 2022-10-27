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