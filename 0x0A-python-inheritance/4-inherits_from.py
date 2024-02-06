#!/usr/bin/python3
"""Defines an inherited class-checking function."""


def inherits_from(obj, a_class):
    """
    Args:
        obj: object to check.
        a_class: class to compare against.

    Returns:
        bool: True if obj is an instance of a_class or its subclass,
        False otherwise.
    """
    return (isinstance(obj, a_class) and type(obj) != a_class)
