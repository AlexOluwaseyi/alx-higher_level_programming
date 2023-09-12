#!/usr/bin/python3

"""
Write and append text to a file
"""


def append_write(filename="", text=""):
    """
    Append text to a file

    Args:
        filename (str): file to append text to
        text (str): string of text to be added at the end of the file

    Return:
        number of characters appended.
    """
    with open(filename, 'a+', encoding='utf-8') as file:
        return file.write(text)
