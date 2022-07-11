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
        if id is not None:
            self.id = id
        else:
            __nb_objects += 1
            self.id = __nb_objects

    def to_json_string(list_dictionaries):
        import json

        if list_dictionaries is None:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    def save_to_file(cls, list_objs):
        pass
