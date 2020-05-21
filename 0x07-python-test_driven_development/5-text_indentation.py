#!/usr/bin/python3
""" prints double line when it hits certain chars"""


def text_indentation(text):
    """text indent funciton"""
    if type(text) is not str:
        raise TypeError("text must be a string")
    beg = 1
    for char in text:
        if beg is 1 and char is " ":
            beg = 0
            pass
        else:
            print(char, end="")
            beg = 0
        if char is '.' or char is '?' or char is ':':
            print("\n")
            beg = 1
