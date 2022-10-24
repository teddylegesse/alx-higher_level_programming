#!/usr/bin/python3
"""Class MyInt that inherits from int"""


class MyInt(int):
    """Definition of class MyInt that inherits from class int"""

    def __eq__(self, value):
        """Overrides equals, inverting it"""
        return self.real != value

    def __ne__(self, value):
        """Overrides not-equals, inverting it"""
        return self.real == valu
