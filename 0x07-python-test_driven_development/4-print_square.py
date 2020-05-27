#!/usr/bin/python3
"""print square func for testing"""


def print_square(size):
    """print square function """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(0, size):
        for j in range(0, size):
            print("#", end="")
        print("")
    if size is 0:
        print("", end="")
