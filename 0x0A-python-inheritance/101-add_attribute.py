#!/usr/bin/python3
""" function file for set attribute method """


def add_attribute(self, name, value):
    """ sets attribute"""
    if hasattr(self, "__dict__") is False:
        raise TypeError("can't add new attribute")
    self.__setattr__(name, value)
