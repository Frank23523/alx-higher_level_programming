#!/usr/bin/python3
"""Defines a Python class-to-JSON function."""


def class_to_json(obj):
    """
    Converts an object into a dictionary suitable for JSON serialization.
    Return:
     		the dictionary represntation of a simple data structure
    """
    return (obj.__dict__)
