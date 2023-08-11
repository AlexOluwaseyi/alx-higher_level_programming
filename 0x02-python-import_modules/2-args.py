#!/usr/bin/python3

from sys import argv
if __name__ == "__main__":
    n = len(argv)

    if n > 2:
        print("{:d} arguments:".format(n - 1))
        for i in range(n):
            if i > 0:
                print("{:d}: {}".format(i, argv[i]))
    elif n == 2:
        print("{:d} argument:".format(n - 1))
        for i in range(n):
            if i > 0:
                print("{:d}: {}".format(i, argv[i]))
    elif n == 1:
        print("{:d} arguments.".format(n - 1))
