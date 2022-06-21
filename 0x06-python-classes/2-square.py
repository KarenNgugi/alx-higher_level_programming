#!/usr/bin/python3
"""
module documentation
"""


class Square:
    """
    Square class
    """
    def __init__(self, size=0):
        try:
            if size >= 0 and size.isdigit():
                self.__size = size
            elif size < 0 and size.isdigit():
                raise ValueError
            else:
                raise TypeError
        except TypeError:
            print("size must be an integer")
        except ValueError:
            print("size must be >= 0")
