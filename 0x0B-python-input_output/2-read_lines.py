#!/usr/bin/python3
""" reads n lines from file"""


def read_lines(filename="", nb_lines=0):
    """ reads nb_lines from filename file """
    if nb_lines <= 0:
        nb_lines = 100000
    with open(filename, 'r') as f:
        for i in range(0, nb_lines):
            line = f.readline()
            if line != "":
                print(line, end="")
            else:
                break
