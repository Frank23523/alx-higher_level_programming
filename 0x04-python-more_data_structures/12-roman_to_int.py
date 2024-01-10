#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None or type(roman_string) != str:
        return 0
    roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    solution = 0
    prev_val = 0
    for c in roman_string:
        current_val = roman_dict.get(c, 0)
        if current_val == 0:
            return 0
        if current_val > prev_val:
            solution += current_val - 2 * prev_val
        else:
            solution += current_val
        prev_val = current_val
    return solution
