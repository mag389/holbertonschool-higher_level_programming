#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    newdict = dict(a_dictionary)
    for (x, v) in newdict.items():
        if v is value:
            a_dictionary.pop(x, None)
    return a_dictionary
