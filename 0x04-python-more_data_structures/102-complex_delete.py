#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    for (x, v) in dict(a_dictionary).items():
        if v is value:
            a_dictionary.pop(x, None)
    return a_dictionary
