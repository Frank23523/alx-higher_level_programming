#!/usr/bin/python3
""" models/base.py """


class Base:
    """
    Base class for managing id attribute in all future classes

    Private Class Attributes: __nb_objects
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """ This initializes Base class. """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
