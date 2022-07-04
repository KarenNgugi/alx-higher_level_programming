#!/usr/bin/python3
"""
5-base_geometry module
"""


class BaseGeometry:
    """
    public method "area"
    """
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if type(value) != int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """
    Rectangle class that extends BaseGeometry class
    """
    def __init__(self, width, height):
        if super().integer_validator("width", width):
            self.__width = width
        if super().integer_validator("height", height):
            self.__height = height

    def __str__(self):
        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)

    def __print__(self):
        print("[Rectangle] {:d}/{:d}".format(self.__width, self.__height))

    def area(self):
        return self.__height * self.__width
