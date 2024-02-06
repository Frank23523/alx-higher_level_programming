#!/usr/bin/python3
"""Defines a class-checking function."""


def is_same_class(obj, a_class):
    """
    Args:
        obj: object to check.
        a_class: class to compare against.

    Returns:
        bool: True if obj is an instance of a_class,
        False otherwise.
    """
    return type(obj) is a_class
