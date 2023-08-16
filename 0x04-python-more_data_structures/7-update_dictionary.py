#!/usr/bin/python3

def update_dictionary(a_dictionary, key, value):
    key_list = list(a_dictionary.keys())
    if key in key_list:
        a_dictionary[key] = value
    else:
        a_dictionary[key] = value
    return a_dictionary
