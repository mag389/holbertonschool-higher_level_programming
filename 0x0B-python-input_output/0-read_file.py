#!/usr/bin/python3
""" read file and print"""


def read_file(filename=""):
    """ read file finction """
    with open(filename, 'r') as f:
        read_data = f.read()
    f.closed
    print(read_data)
