#!/usr/bin/python3
"""
module documentation
"""


class Square:
    """
    Square documentation
    """
    def __init__(self, size=0):
        try:
            if type(size) == int:
                if size >= 0:
                    self.__size = size
                else:
                    raise ValueError
            else:
                raise TypeError
        except TypeError:
            print("size must be an integer")
        except ValueError:
            print("size must be >= 0")

    def area(self):
        return self.__size * self.__size
