#!/usr/bin/python3
""" the locked class """


class LockedClass(object):
    """ the class itself """

    def __setattr__(self, name, value):
        """ over rides the setattr thing """
        if name != "first_name":
            raise AttributeError("object has no attribute '{}'".format(name))
        super(LockedClass, self).__setattr__(name, value)
