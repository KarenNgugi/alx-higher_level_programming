#!/usr/bin/python3
import calculator_1
import sys

num_args = len(sys.argv) - 1
c = calculator_1

if num_args != 3:
    print("Usage: ./100-my_calculator.py <a> <operator> <b>")
    sys.exit(1)

a = int(sys.argv[1])
b = int(sys.argv[3])
op = sys.argv[2]

if op == '+':
    print("{} {} {} = {}".format(a, op, b, c.add(a, b)))
elif op == '-':
    print("{} {} {} = {}".format(a, op, b, c.sub(a, b)))
elif op == '*':
    print("{} {} {} = {}".format(a, op, b, c.mul(a, b)))
elif op == '/':
    print("{} {} {} = {}".format(a, op, b, c.div(a, b)))
else:
    print("Unknown operator. Available operators: +, -, * and /")
    sys.exit(1)
