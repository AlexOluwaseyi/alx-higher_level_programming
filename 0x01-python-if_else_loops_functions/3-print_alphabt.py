#!/usr/bin/python3

for i in range(97, 123):
    if chr(i).format() != "e" and chr(i).format() != "q":
        print(chr(i).format(), end="")
