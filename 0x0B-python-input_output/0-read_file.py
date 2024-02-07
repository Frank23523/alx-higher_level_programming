#!/usr/bin/python3
"""A text file-reading function"""


def read_file(filename=""):
    """Reads and prints the contents of a UTF-8 text file to stdout"""
    with open(filename, encoding="utf-8") as file:
        print(file.read(), end="")
