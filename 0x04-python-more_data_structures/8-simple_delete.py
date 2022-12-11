#!/usr/bin/python3
def simple_delete(a_dictionary, key):
    res = a_dictionary.pop(key,"None")
    return res