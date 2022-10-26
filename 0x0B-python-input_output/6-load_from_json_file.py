#!/usr/bin/python3
"""
This module creates an object from json file
"""


import json


def load_from_json_file(filename):
    """Receives filename and returns an JSON object from a recieved file"""
    with open(filename, 'r', encoding='UTF8') as f:
         return json.load(f)
