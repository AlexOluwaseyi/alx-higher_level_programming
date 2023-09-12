#!/usr/bin/python3

"""
A script to illustrate a class inheriting 'list'
"""


class MyList(list):
    """
    A custom list class that inherits the built-in list class.

    Public Methods:
        - print_sorted(self): Prints the list in ascending sorted order.
    """
    def print_sorted(self):
        """
        Prints the list in ascending sorted order.
        """
        sorted_list = sorted(self)
        print(sorted_list)
