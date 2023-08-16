#!/usr/bin/python3

def uniq_add(my_list=[]):
    uniq_list = []
    total = 0
    for n in my_list:
        if n not in uniq_list:
            uniq_list.append(n)
            total += n
    return total
