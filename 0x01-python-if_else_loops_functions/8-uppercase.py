#!/usr/bin/python3
def uppercase(str):
    s = ""
    for i in str:
        if i.islower():
            s += chr(ord(i) - 32)
        else:
            s += i
    print(s)
