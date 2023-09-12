#!/usr/bin/python3
"""
Converts objects to JSON
"""


import json
""" import JSON module for python """


def to_json_string(my_obj):
    """
    Converts an object to JSON

    Agrs:
        my_obj: Object to be converted to JSON

    Return:
        JSON
    """
    return json.dump(my_obj)
