#!/usr/bin/python3

"""
A script to illustrate a class inheriting from list
"""

class MyList(list):
    """
    A custom list class that inherits from the built-in list class.

    Pycodestyle (PEP8) Compliance:
    - Class names are written in CamelCase.
    - Methods are written in lowercase with words separated by underscores.
    - Opening and closing parentheses in method definitions are not spaced.
    - Method docstrings are enclosed in triple quotes.

    Public Methods:
        - print_sorted(self): Prints the list in ascending sorted order.
    """
    def print_sorted(self):
        """
        Prints the list in ascending sorted order.
        """
        sorted_list = sorted(self)
        print(sorted_list)
