#!/usr/bin/python3
import sys
import json


def save_to_json_file(my_obj, filename):
    """Write a given object to a text file using its JSON representation"""
    with open(filename, "w") as file:
        json.dump(my_obj, file)


def load_from_json_file(filename):
    """
    Reads a JSON file and returns the Python data structure
    Returns:
        object: The Python data structure represented by the JSON content
    """
    with open(filename) as file:
        return json.load(file)


if __name__ == "__main__":
    try:
        existing_data = load_from_json_file("add_item.json")
    except FileNotFoundError:
        existing_data = []
    new_items = sys.argv[1:]
    existing_data.extend(new_items)
    save_to_json_file(existing_data, "add_item.json")
    print(f"Added {len(new_items)} items to add_item.json.")
