#!/usr/bin/python3
"""
module for printing the hwole name
"""


def say_my_name(first_name, last_name=""):
    """say my name function"""
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    print("{} {}".format(first_name, last_name))
