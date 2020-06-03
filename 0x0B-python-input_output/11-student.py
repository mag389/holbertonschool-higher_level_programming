#!/usr/bin/python3
""" the student class file """


class Student:
    """ the student class """

    def __init__(self, first_name, last_name, age):
        """ instantiation with name and age """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ returns dict definition of a student"""
        return self.__dict__
