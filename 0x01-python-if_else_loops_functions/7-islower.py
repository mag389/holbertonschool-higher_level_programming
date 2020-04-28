#!/bin/usr/python3
# islower - determines letter case
# @c: the letter to test
# Return: true or false
def islower(c):
    if ord(c) > 96 and ord(c) < 124:
        return(True)
    return(False)
