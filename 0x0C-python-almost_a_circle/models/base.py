#!/usr/bin/python3
""" the base class file in the models folder """
import json


class Base:
    """ the Base class """

    _nb_objects = 0

    def __init__(self, id=None):
        """ instantiation method
        each has an integer id
        """
        if id is not None:
            self.id = id
        else:
            Base._nb_objects += 1
            self.id = Base._nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON rep of list dicts"""
        if list_dictionaries is None or len(list_dictionaries) is 0:
            return []
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ saves list of objects to json file """
        if list_objs is None:
            list_objs = []
        dict_list = []
        for item in list_objs:
            dict_list.append(cls.to_dictionary(item))
        json_list = Base.to_json_string(dict_list)
        if cls.__name__ == "Rectangle":
            filename = "Rectangle.json"
        else:
            filename = "Square.json"
        with open(filename, 'w') as f:
            f.write(json_list)

    @staticmethod
    def from_json_string(json_string):
        """ takes json string, makes those objects """
        if json_string is None or len(json_string) is 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ returns an instance with attributes already set """
        dummy = cls(1, 1, 0, 0)
        dummy.update(dictionary)
        return dummy
