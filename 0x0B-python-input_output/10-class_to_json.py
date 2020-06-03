#!/usr/bin/python3
""" returns dict description for json serialization """


def class_to_json(obj):
    """ the function to do so"""
    return obj.__dict__
