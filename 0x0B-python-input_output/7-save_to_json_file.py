#!/usr/bin/python3
""" saves object to json file as string"""
import json


def save_to_json_file(my_obj, filename):
    """ saves string rep of my_obj to file filename """
    with open(filename, 'w') as f:
        string = json.dumps(my_obj)
        f.write(string)
