#!/usr/bin/python3
"""
5-text_indentation module
"""


def text_indentation(text):
    """
    Prints 2 new lines after each of these characters:
        - .
        - ?
        - :
    """
    if type(text) != str:
        raise TypeError("text must be a string")
    for char in text:
        print(char, end="")
        if char == '.' or char == '?' or char == ':':
            print('\n')
