#!/usr/bin/python3
"""models/square.py"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Square class representing a square
    Inherits from the Rectangle class.
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Constructor for Square class

        Args:
            size (int): size of the Square.
            x (int): X-coordinate of the Square.
            y (int): Y-coordinate of the Square.
            id (int): unique identitifier
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ Overriding __str__ """
        return (f"[Square] ({self.id}) {self.x}/{self.y}"
                f" - {self.width}")

    @property
    def size(self):
        return (self.width)

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """
        Assigns an argument to each attribute

        Args:
            *args: variable arguments in order: id, size, x, y
            **kwargs: "double pointer" to a dictionary: key/value
        """
        if args:
            attrs = ["id", "size", "x", "y"]
            for i, value in enumerate(args):
                setattr(self, attrs[i], value)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)
