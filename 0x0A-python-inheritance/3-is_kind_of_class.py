#!/usr/bin/python3

"""To determine if an onject is an instance of"""


def is_kind_of_class(obj, a_class):
    """
    Returns True if obj is an instance of, or if the object is
    an instance of a class that inherited from, the
    specified class; otherwise False.

    Args:
        obj: The object to be checked.
        a_class: The class to check against.

    Returns:
        True if obj is an instance of a_class or any subclass,
        False otherwise.
    """
    return isinstance(obj, a_class)
