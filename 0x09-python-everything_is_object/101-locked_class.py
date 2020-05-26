#!/usr/bin/python3
""" the locked class """


class LockedClass(object):
    """ the class itself """

    __slots__ = ['first_name']

    def __init__(self):
        """ init function, does nothing"""
        return

    def __setattr__(self, name, value):
        """ over rides the setattr thing """
        if name != "first_name":
            raise AttributeError("'LockedClass' object has no attribute \
'{}'".format(name))
        super(LockedClass, self).__setattr__(name, value)
