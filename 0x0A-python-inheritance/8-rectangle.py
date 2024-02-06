#!/usr/bin/python3
"""Class Rectangle that inherits from BaseGeometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Represent a rectangle"""

    def __init__(self, width, height):
        """Intialize a new Rectangle.

        Args:
            width (int): The width of the Rectangle.
            height (int): The height of the Rectangle.
        Raises:
            TypeError: If width or height is not a positive integer
        """
        self.__width = self.integer_validator("width", width)
        self.__height = self.integer_validator("height", height)
