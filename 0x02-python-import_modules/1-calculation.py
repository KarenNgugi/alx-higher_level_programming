#!/usr/bin/python3
import calculator_1

a = 10
b = 5
func = calculator_1
print("{} + {} = {}".format(a, b, func.add(a, b)))
print("{} + {} = {}".format(a, b, func.sub(a, b)))
print("{} + {} = {}".format(a, b, func.mul(a, b)))
print("{} + {} = {}".format(a, b, func.div(a, b)))
