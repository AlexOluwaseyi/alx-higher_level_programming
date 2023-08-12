#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a) > 0:
        x1 = tuple_a[0]
        if len(tuple_a) > 1:
            x2 = tuple_a[1]
        else:
            x2 = 0
    else:
        x1 = 0
        x2 = 0

    if len(tuple_b) > 0:
        y1 = tuple_b[0]
        if len(tuple_b) > 1:
            y2 = tuple_b[1]
        else:
            y2 = 0
    else:
        y1 = 0
        y2 = 0

    new_tuple = (x1 + y1, x2 + y2)
    return new_tuple
