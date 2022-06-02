#!/usr/bin/python3
import sys

num_args = len(sys.argv)
sum = 0

if num_args > 1:
    for i in range(1, num_args):
        sum += int(sys.argv[i])

print(sum)
