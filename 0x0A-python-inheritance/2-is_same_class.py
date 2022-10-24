#!/usr/bin/python3
"""
Module for is_same_class method
"""

def is_same_class(obj, a_class):
    """ Check if is a same class: return TRUE"""
    if type(obj) == a_class:
        return True
    else:
        return False
