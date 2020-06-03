#!/usr/bin/python3
""" write to file appends mode"""


def append_write(filename="", text=""):
    """ write to file, appends if it exists """
    with open(filename, 'a') as f:
        num_chars = f.write(text)
    return num_chars
