#!/usr/bin/python3
""" returns number of lines in file """


def number_of_lines(filename=""):
    """ returns number of lines in the file """
    lines = 0
    with open(filename, 'r') as f:
        for line in f:
            lines += 1
    f.closed
    return lines
