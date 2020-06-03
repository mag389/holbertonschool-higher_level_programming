#!/usr/bin/python3
""" file for json conversion function """
import json


def from_json_string(my_str):
    """converts to object from json string"""
    return json.loads(my_str)
