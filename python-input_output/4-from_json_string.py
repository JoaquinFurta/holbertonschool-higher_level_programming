#!/usr/bin/python3
"""function that returns an object (Python data structure)
    represented by a JSON string"""


import json


def from_json_string(my_str):
    """ it recives a string as a parameter"""
    return json.loads(my_str)
