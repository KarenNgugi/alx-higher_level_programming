#!/usr/bin/python3
"""
base module
"""

class Base:
    """
    base class
    """

    global __nb_objects
    __nb_objects = 0

    def __init__(self, id=None):
        global __nb_objects
        if id != None:
            self.id = id
        else:
            __nb_objects += 1
            self.id = __nb_objects
