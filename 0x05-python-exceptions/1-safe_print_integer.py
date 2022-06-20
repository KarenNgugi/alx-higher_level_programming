#!/usr/bin/python3
def safe_print_integer(value):
    isDigit = True
    try:
        if str(abs(value)).isdigit():
            print("{:d}".format(value))
        else:
            isDigit = False
        return isDigit
    except TypeError:
        pass
