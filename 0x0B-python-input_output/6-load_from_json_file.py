#!/usr/bin/python3
"""A JSON file-reading function."""
import json


def load_from_json_file(filename):
    """
    Reads a JSON file and returns the Python data structure
    Returns:
        object: The Python data structure represented by the JSON content
    """
    with open(filename) as file:
        return json.load(file)
