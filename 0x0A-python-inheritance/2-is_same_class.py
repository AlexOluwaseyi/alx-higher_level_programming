#!/usr/bin/python3

"""To shows if classes are same or not"""


def is_same_class(obj, a_class):
    """
    Returns True if obj is exactly an instance of the specified class;
    otherwise False.

    Args:
        obj: The object to be checked.
        a_class: The class to check against.

    Returns:
        True if obj is an instance of a_class, False otherwise.
    """
    return type(obj) == a_class
