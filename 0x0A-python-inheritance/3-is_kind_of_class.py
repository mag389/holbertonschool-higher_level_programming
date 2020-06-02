#!/usr/bin/python3
""" tests for instance of class or subclass"""


def is_kind_of_class(obj, a_class):
    """ is it the class or a subclass """
    return issubclass(type(obj), a_class)
