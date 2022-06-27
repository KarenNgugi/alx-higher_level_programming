#!/usr/bin/python3
"""
1-rectangle module
"""


class Rectangle:
    """
    rectangle class
    """
    def __init__(self, width=0, height=0):
        if type(height) == int:
            if height >= 0:
                self.__height = height
            else:
                raise TypeError("height must be >= 0")
        else:
            raise TypeError("height must be an integer")

        if type(width) == int:
            if width >= 0:
                self.__width = width
            else:
                raise TypeError("width must be >= 0")
        else:
            raise TypeError("width must be an integer")

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) == int:
            if value >= 0:
                self.__height = value
            else:
                raise TypeError("height must be >= 0")
        else:
            raise TypeError("height must be an integer")

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) == int:
            if value >= 0:
                self.__width = value
            else:
                raise TypeError("width must be >= 0")
        else:
            raise TypeError("width must be an integer")

    def area(self):
        return self.__height * self.__width

    def perimeter(self):
        h = 2 * self.__height
        w = 2 * self.__width
        return h + w
