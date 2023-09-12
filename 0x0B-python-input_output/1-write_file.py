#!/usr/bin/python3
"""
Write to a file
"""

def write_file(filename="", text=""):
    """
    Function write texts to an open file

    Args:
        filename (str): name of hte file to be writtent to
        text (str): string to be writtent to file

    Return:
        Number of characters written to the file
    """
    with open(filename, 'w+', encoding='utf-8') as file:
       return file.write(text)
