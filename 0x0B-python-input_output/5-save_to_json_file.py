#!/usr/bin/python3
"""
Save JSON to file
"""


import json
""" import JSON module for python """


def save_to_json_file(my_obj, filename):
    """
    Save JSON represetation to file

    Agrs:
        my_obj: Object to be converted to JSON
        filename: Destination file where JSON would be saved to

    Return:
        JSON.dump(my_obj, filename)
    """
    with open(filename, 'w+', encoding='utf-8') as filename:
        return json.dump(my_obj, filename)
