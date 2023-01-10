#!/usr/bin/python3

""" File name : 4-from_json_string.py
"""
import json


def from_json_string(my_str):
    """from_json_string  returns an object
    (Python data structure) represented by a JSON string

    Args:
        my_str (obj): any object for example list, dict
    """
    return(json.loads(my_str))
