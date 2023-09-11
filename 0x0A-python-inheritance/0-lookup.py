#!/usr/bin/python3


def lookup(obj):
    """
    Returns a list of available attributes and methods of an object.

    Args:
        obj: The object to look up.

    Returns:
        A list of strings representing the attributes and methods.
    """
    attributes_and_methods = [attr for attr in dir(obj)]

    return attributes_and_methods
