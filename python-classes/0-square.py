#!/usr/bin/python3
"""
This module defines a Square class that represents a square with a private size.
"""


class Square:
    """
    A class that represents a square using a private size attribute.
    """

    def __init__(self, size):
        """
        Initialize a Square instance.

        Args:
            size (int): The size of the square.
        """
        self.__size = size
