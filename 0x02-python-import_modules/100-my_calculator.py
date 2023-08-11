#!/usr/bin/python3

from calculator_1 import add, sub, mul, div
from sys import argv
import sys

if __name__ == "__main__":
    number_args = len(argv)
    operators = ["+", "-", "/", "*"]

    if number_args != 4:
        print("Usage: {} <a> <operator> <b>".format(argv[0]))
        sys.exit(1)
    else:
        try:
            a = int(argv[1])
            b = int(argv[3])
        except ValueError:
            print("Both {} and {} should be integers".format(argv[1], argv[3]))
            sys.exit(1)
        operator = argv[2]

        if operator not in operators:
            print("Unknown operator. Available operators: +, -, * and /")
            sys.exit(1)

        elif argv[1].isdigit() and argv[3].isdigit():
            index = operators.index(operator)
            if index == 0:
                result = add(a, b)
            elif index == 1:
                result = sub(a, b)
            elif index == 2:
                result = mul(a, b)
            else:
                result = div(a, b)
            print("{:d} {:s} {:d} = {:d}".format(a, operator, b, result))
            sys.exit(0)
