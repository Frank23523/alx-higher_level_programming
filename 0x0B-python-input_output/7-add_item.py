#!/usr/bin/python3
import sys
import json

if __name__ == "__main__":
    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
    load_from_json_file = \
        __import__('6-load_from_json_file').load_from_json_file

    try:
        existing_data = load_from_json_file("add_item.json")
    except FileNotFoundError:
        existing_data = []
    existing_data.extend(sys.argv[1:])
    save_to_json_file(existing_data, "add_item.json")
