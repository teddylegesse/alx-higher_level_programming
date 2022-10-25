#!/usr/bin/python3
"""function that appends to a text file"""


def append_write(filename="", text=""):
    """function that appends a string at the end of a text file (UTF8)
    Args:
        filename (str): The name of the file to append to.
        text (str): The string to append to the file.
    Returns:
        returns the number of characters added:
    """
    with open(filename, "a", encoding="utf-8") as fname:
        return fname.write(text)
