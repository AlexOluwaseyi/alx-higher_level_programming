#!/usr/bin/python3
"""inherits instance of an a class"""


def inherits_from(obj, a_class):
    """
    Returns True if obj is an instance of a class that inherited
    (directly or indirectly)
    from the specified class; otherwise False.

    Args:
        obj: The object to be checked.
        a_class: The class to check against.

    Returns:
        True if obj is an instance of a subclass, False otherwise.
    """
    return issubclass(type(obj), a_class) and type(obj) != a_class
