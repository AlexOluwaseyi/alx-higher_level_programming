#!/usr/bin/python3
"""
Finds the peak values in an array, returns the last
"""


def find_peak(list_of_integers):
    """ Function protoype to find peak
    """
    length = len(list_of_integers)

    """Returns None when an empty list is provided"""
    if not length:
        return None

    """Initializes peak value with the first item in the list"""
    peak = list_of_integers[0]

    for i in range(1, length):
        if list_of_integers[i] > list_of_integers[i-1]:
            peak = list_of_integers[i]
    return peak
