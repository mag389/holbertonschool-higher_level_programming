#!/usr/bin/python3
""" loads object from json string file """
import json


def load_from_json_file(filename):
    """ loads the object stored as string in file """
    with open(filename, 'r') as f:
        return json.loads(f.read())
