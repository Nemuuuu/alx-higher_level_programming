#!/usr/bin/python3

""" File name : 8-class_to_json.py
"""


def class_to_json(obj):
    """class_to_json return dictionary description with simple data structure

    Args:
        obj : any object for example list, dict
    """
    return obj.__dict__
