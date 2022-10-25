#!/usr/bin/python3
"""define function that writes an Object to a text file"""
import json


def save_to_json_file(my_obj, filename):
    """Write an object to a text file using JSON representation."""
    with open(filename, "w") as fname:
        json.dump(my_obj, fname)
