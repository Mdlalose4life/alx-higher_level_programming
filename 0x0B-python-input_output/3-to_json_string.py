#!/usr/bin/python3
"""
This module returns json representation of an object.
"""


import json


def to_json_string(my_obj):
    """Receives an object and
    returns a json representation of the recieved object."""
    return json.dumps(my_obj)
