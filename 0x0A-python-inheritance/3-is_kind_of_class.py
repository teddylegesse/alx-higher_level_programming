#!/usr/bin/python3
"""
function that returns True if the object is an instance of 
a class that inherited (directly or indirectly) 
from the specified class ; otherwise False.
"""


def is_kind_of_class(obj, a_class):
    """Check instance of object and return true"""

    return (isinstance(obj, a_class))
