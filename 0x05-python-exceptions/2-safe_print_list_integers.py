#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    n = 0
    count = 0
    while n < x:
        try:
            print("{:d}".format(my_list[n]), end="")
            count += 1
        except (TypeError, ValueError):
            pass
        n += 1
    print()
    return count
