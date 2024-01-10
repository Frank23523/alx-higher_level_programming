#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    temp = a_dictionary.copy()
    for key, i in temp.items():
        if value == i:
            a_dictionary.pop(key)
        return a_dictionary
