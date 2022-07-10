#!/usr/bin/python3
"""
square module
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    square class inherits from Rectangle class
    """
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(id, x, y, width, height)
        self.id = id
        self.__width = size
        self.__height = size
        self.__x = x
        self.__y = y

    def __str__(self):
        result1 = "[Square] (" + str(self.id) + ") "
        result2 = str(self.__x) + "/" + str(self.__y) + " - "
        result3 = str(self.__width)
        return result1 + result2 + result3
