#!/usr/bin/python3
def no_c(my_string):
    newstring = ""
    for i in range(0, len(my_string)):
        if my_string[i] is not 'c' and my_string[i] is not 'C':
            newstring += my_string[i]
    return newstring
