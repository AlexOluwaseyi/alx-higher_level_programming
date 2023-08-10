#!/usr/bin/python3

for i in range(99):
    while i != 99:
        print("{0:02d}".format(i), end=", ")
        i += 1
    break
print("{0:02d}".format(i))
