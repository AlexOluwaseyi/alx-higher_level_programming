#!/usr/bin/python3
"""
Creates an object from  JSON file
"""


import json
""" import JSON module for python """


def load_from_json_file(filename):
    """
    Loads a JSON string and create a Python object

    Agrs:
        filename: JSON file to open for creating object

    Return:
        JSON.load(filename)
    """
    with open(filename, 'r', encoding='utf-8') as filename:
        return json.load(filename)
