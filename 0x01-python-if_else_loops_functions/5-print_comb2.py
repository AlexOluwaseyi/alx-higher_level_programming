#!/usr/bin/python3

for i in range(98):
    while i != 98:
          print("{0:02d}".format(i), end=", ")
          i += 1
    break
print("{0:02d}".format(i))
