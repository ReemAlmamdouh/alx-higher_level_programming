#!/usr/bin/python3
"""Json representation of an object"""
import json

def to_json_string(my_obj):
    """Function returns the JSON representation of an object (string)"""

    return json.dump(my_obj)
