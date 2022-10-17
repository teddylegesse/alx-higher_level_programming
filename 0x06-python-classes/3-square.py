#!/usr/bin/python3
"""
module Square class
"""


class Square:
    """attributes of  a square."""

    def __init__(self, size):
        """Initialize a new Square.
        Args:
            size (int): The size of the new square.
        """
	if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

	def area(self):
        """Area of the square.
        Returns:
            thee size squared.
        """
        return self.__size ** 2
