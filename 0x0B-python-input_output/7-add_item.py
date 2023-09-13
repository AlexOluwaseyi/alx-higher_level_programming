#!/usr/bin/python3
"""
 adds all arguments to a Python list, and then save them to a file
"""


import json
import sys
import os
"""
imports:
    json module - save and load json file
    sys module - to use args method
    os module - to find file in path
"""

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


if not os.path.exists('add_item.json'):
    save_to_json_file([], 'add_item.json')

my_list = load_from_json_file('add_item.json')

my_list.extend(sys.argv[1:])

save_to_json_file(my_list, 'add_item.json')
