#!/usr/bin/python3
"""Defines a Rectangle class"""


class Rectangle:
    """This class represent a rectangle"""

    def __init__(self, width=0, height=0):
        """Initialize a new instance of the rectangle"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Gets the width of the Rectangle."""
        return (self.__width)

    @width.setter
    def width(self, value):
        """Sets the width of the Rectangle"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Gets the height of the Rectangle"""
        return (self.__height)

    @height.setter
    def height(self, value):
        """Sets the height of the Rectangle"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calcutates the area of the Rectangle."""
        return (self.__width * self.__height)

    def perimeter(self):
        """Calculates the perimeter of the Rectangle."""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return (2 * (self.__width + self.__height))

    def __str__(self):
        """Return a string representation of the Rectangle"""
        if self.__width == 0 or self.__height == 0:
            return ("")
        return ("\n".join(["#" * self.width] * self.height))

    def __repr__(self):
        """Return a string representation of the Rectangle"""
        return ("Rectangle({}, {})".format(self.width, self.height))
