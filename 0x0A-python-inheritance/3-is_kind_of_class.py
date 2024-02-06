#!/usr/bin/python3
"""Defines a class and inherited class-checking function"""


def is_kind_of_class(obj, a_class):
    """
    Args:
        obj: object to check.
        a_class: class to compare against.

    Returns:
        bool: True if obj is an instance of a_class or its subclass,
        False otherwise.
    """
    return isinstance(obj, a_class)
