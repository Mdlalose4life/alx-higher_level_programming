#!/usr/bin/python3
"""
This module writes an object to a textfile using a json format
"""


import json


def save_to_json_file(my_obj, filename):
    """Receives an object and a file and writes an object to a textfile using a json format"""
    with open(filename, 'w', encoding='UTF8') as f:
        json.dump(my_obj, f)
