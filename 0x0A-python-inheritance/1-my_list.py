#!/usr/bin/python3
"""Defines an inherited list class"""


class MyList(list):
    """Executes sorted printing for built-in list class"""
    def print_sorted(self):
        print(sorted(self))
