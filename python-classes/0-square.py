#!/usr/bin/python3
"""
This module defines a Square class that represents a square with a private size.
"""

class Square:
    """
    A class to represent a square.

    Attributes:
        __size (int): The size of the square, stored privately.
    """

    def __init__(self, size):
        """
        Initialize a new Square instance.

        Args:
            size (int): The size of the square.
        """
        self.__size = size
