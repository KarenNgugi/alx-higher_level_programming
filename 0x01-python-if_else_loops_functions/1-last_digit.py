#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
modulo = abs(number) % 10
if modulo > 5:
    print(f"Last digit of {number:d} is {modulo:d} and is greater than 5")
elif modulo < 6 and modulo != 0:
    print(f"Last digit of {number:d} is {modulo:d} and is less than 6 and not 0")
elif modulo == 0:
    print(f"Last digit of {number:d} is {modulo:d} and is 0")
