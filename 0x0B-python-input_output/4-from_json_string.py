#!/usr/bin/python3
"""
This module returns an object representation by a JSON string.
"""


import json


def from_json_string(my_str):
    """Receives a string and
    returns a JSON string representation of the recieved string."""
    return json.loads(my_str)
