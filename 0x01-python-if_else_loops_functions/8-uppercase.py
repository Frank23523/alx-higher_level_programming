#!/usr/bin/python3
def uppercase(str):
    for letter in str:
        if 'a' <= letter <= 'z':
            u_letter = chr(ord(letter) - ord('a') + ord('A'))
        else:
            u_letter = letter
        print(u_letter, end='')
    print()
