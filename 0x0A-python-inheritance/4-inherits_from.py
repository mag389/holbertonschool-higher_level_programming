#!/usr/bin/python3
""" inheriting but not instance """


def inherits_from(obj, a_class):
    """ inherit sfrom function """
    return issubclass(type(obj), a_class) and type(obj) != a_class
