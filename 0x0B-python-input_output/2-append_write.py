#!/usr/bin/python3
"""A file-appending function"""


def append_write(filename="", text=""):
    """Appends the given text to a UTF-8 text file

    Args:
        filename (str): The name of the file to append to.
        text (str): The string to append to the file.
    Returns:
        The number of characters added
    """
    with open(filename, "a", encoding="utf-8") as file:
        return file.write(text)
