#!/usr/bin/python3

def replace_in_list(my_list, idx, element):
    n = len(my_list) - 1
    if 0 <= idx <= n:
        my_list[idx] = element
        return my_list
    else:
        return my_list
