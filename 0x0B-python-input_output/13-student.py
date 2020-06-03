#!/usr/bin/python3
""" the student class file """


class Student:
    """ the student class """

    def __init__(self, first_name, last_name, age):
        """ instantiation with name and age """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ returns dict definition of a student"""
        if attrs is None:
            return self.__dict__
        if type(attrs) is not list:
            return self.__dict__
        for elem in attrs:
            if type(elem) is not str:
                return self.__dict__
        newdict = {}
        for elem in attrs:
            try:
                newdict[elem] = self.__dict__[elem]
            except:
                pass
        return newdict

    def reload_from_json(self, json):
        """ reloads object from json"""
        self.__dict__ = json
        for item in json:
            setattr(self, item, json[item])
