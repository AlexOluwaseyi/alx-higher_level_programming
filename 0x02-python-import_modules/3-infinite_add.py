#!/usr/bin/python3

from sys import argv
if __name__ == "__main__":
    n = len(argv)
    sum = 0

    if n == 1:
        sum
    elif n > 1:
        for i in range(1, n):
            sum += int(argv[i])
#            if int(argv[i]) > 0:
#                sum += int(argv[i])
#            else:
#                sum -= int(argv[i])
    print("{:d}".format(sum))
