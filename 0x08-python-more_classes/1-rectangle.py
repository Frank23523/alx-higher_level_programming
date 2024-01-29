#!/usr/bin/python3
"""Defines a rectangle class"""


class Rectangle:
    """This class defines a Rectangle"""

    def __init__(self, width=0, height=0):
        """Initializes a new instance of the Rectangle class

        Private instance attribute:
            - width: width of the rectangle.
            - height: height of the rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Gets the width of the rectangle."""
        return self._width

    @width.setter
    def width(self, value):
        """Sets the width of the rectangle."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self._width = value

    @property
    def height(self):
        """Gets the height of the rectangle."""
        return self._height

    @height.setter
    def height(self, value):
        """Sets the height of the rectangle."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self._height = value
