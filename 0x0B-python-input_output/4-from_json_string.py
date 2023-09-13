#!/usr/bin/python3
"""
Returns an objects from JSON
"""


import json
""" import JSON module for python """


def from_json_string(my_str):
    """
    Converts an object to JSON

    Agrs:
        my_str: Object to be converted to JSON

    Return:
        json.loads(my_str)
    """
    return json.loads(my_str)
