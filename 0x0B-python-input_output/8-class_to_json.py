#!/usr/bin/python3

"""
function that returns the dictionary description
with simple data structure
"""


def class_to_json(obj):
    """
    Convert an object with serializable attributes to a dictionary.

    Args:
        obj: An instance of a Class.

    Returns:
        dict: A dictionary description of the object.
    """
    if not hasattr(obj, '__dict__'):
        raise ValueError("Input object must be an instance of a Class.")

    return obj.__dict__
