#!/usr/bin/python3
"""
retangle module
"""
from models.base import Base


class Rectangle(Base):
    """
    rectangle class which inherits from base class
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.id = self.id

        if type(width) == int:
            if width > 0:
                self.__width = width
            else:
                raise ValueError("width must be > 0")
        else:
            raise TypeError("width must be an integer")

        if type(height) == int:
            if height > 0:
                self.__height = height
            else:
                raise ValueError("height must be > 0")
        else:
            raise TypeError("height must be an integer")

        if type(x) == int:
            if x >= 0:
                self.__x = x
            else:
                raise ValueError("x must be >= 0")
        else:
            raise TypeError("x must be an integer")

        if type(y) == int:
            if y >= 0:
                self.__y = y
            else:
                raise ValueError("y must be >= 0")
        else:
            raise TypeError("y must be an integer")

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, val):
        if type(val) == int:
            if val > 0:
                self.__width = val
            else:
                raise ValueError("width must be > 0")
        else:
            raise TypeError("width must be an integer")

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, val):
        if type(val) == int:
            if val > 0:
                self.__height = val
            else:
                raise ValueError("height must be > 0")
        else:
            raise TypeError("height must be an integer")

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, val):
        if type(val) == int:
            if val >= 0:
                self.__x = val
            else:
                raise ValueError("x must be >= 0")
        else:
            raise TypeError("x must be an integer")

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, val):
        if type(val) == int:
            if val >= 0:
                self.__y = val
            else:
                raise ValueError("y must be >= 0")
        else:
            raise TypeError("y must be an integer")

    def area(self):
        return self.__width * self.__height

    def display(self):
        res = ""
        for row in range(self.__y - 1):
            print("\n")
        for row in range(self.__height):
            res += (" " * self.__x) + ("#" * self.__width) + "\n"
        print(res[:-1])

    def __str__(self):
        result1 = "[Rectangle] (" + str(self.id) + ") "
        result2 = str(self.__x) + "/" + str(self.__y) + " - "
        result3 = str(self.__width) + "/" + str(self.__height)
        return result1 + result2 + result3

    def update(self, *args):
