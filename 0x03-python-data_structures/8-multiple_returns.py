#!/usr/bin/python3
def multiple_returns(sentence):
    if len(sentence) > 0:
        first_char = sentence[0]
    else:
        None
    return (len(sentence), first_char)
