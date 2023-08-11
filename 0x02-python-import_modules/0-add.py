#!/usr/bin/python3

from add_0 import add
if __name__ == "__main__":
    a = 1
    b = 2

    add(a, b)

    print("{} + {} = {}".format(a, b, add(a, b)))
