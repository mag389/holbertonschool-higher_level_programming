#!/usr/bin/python3
""" writing text to  file """


def write_file(filename="", text=""):
    """ writes to file, overwrites if file exists, creates if it doesn't """
    with open(filename, 'w') as f:
        c = f.write(text)
    return c
