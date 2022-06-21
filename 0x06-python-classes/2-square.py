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
            if str(abs(size)).isdigit():
                try:
                    if size >= 0:
                        self.__size = size
                    else:
                        raise ValueError
                except ValueError:
                    print("size must be >= 0")
            else:
                raise TypeError
        except TypeError:
            print("size must be an integer")
