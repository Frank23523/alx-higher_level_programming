#!/usr/bin/python3
"""Defines a text-indentation function."""


def text_indentation(text):
    """Prints a text with 2 new lines after each of these: ., ? and :

    Args:
        text (str): The text to print.
    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    ele = 0
    while ele < len(text) and text[ele] == ' ':
        ele += 1

    while ele < len(text):
        print(text[ele], end="")
        if text[ele] == "\n" or text[ele] in ".?:":
            if text[ele] in ".?:":
                print("\n")
            ele += 1
            while ele < len(text) and text[ele] == ' ':
                ele += 1
            continue
        ele += 1
