#!/usr/bin/python3
""" the base class file in the models folder """
import json
import csv
import turtle


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
            return "[]"
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
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1, 0, 0)
        else:
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """ loads objects as json strings from file, makes them as objs """
        retlist = []
        filename = cls.__name__ + ".json"
        try:
            with open(filename, 'r') as f:
                text = f.read()
        except:
            return []
        jsontxt = cls.from_json_string(text)
        for item in jsontxt:
            retlist.append(cls.create(**item))
        return retlist

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """ saves objects to file, but a csv file"""
        if list_objs is None:
            list_objs = []
        dict_list = []
        for item in list_objs:
            dict_list.append(cls.to_dictionary(item))
        filename = cls.__name__ + ".csv"
        if cls.__name__ == "Rectangle":
            fieldnames = ["id", "width", "height", "x", "y"]
        else:
            fieldnames = ["id", "size", "x", "y"]
#        print(fieldnames)
        with open(filename, "w") as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            for dictrow in dict_list:
                writer.writerow(dictrow)

    @classmethod
    def load_from_file_csv(cls):
        """ loads objects from csv file """
        retlist = []
        filename = cls.__name__ + ".csv"
        dictlist = []
        try:
            with open(filename, "r") as f:
                reader = csv.DictReader(f)
                for row in reader:
                    # print(row)
                    # print(type(row))
                    dictlist.append(row)
        except:
            return []
        for row in dictlist:
            for key in row:
                row[key] = int(row[key])
        obj_list = []
        for row in dictlist:
            obj_list.append(cls.create(**row))
        return obj_list

    @staticmethod
    def draw(list_rectangles, list_squares):
        """ draws the shapes with turtles """
        tim = turtle.Turtle()
        tim.color('red')
        tim.pensize(2)
        tim.shape('turtle')
        mag = 1

        for rect in list_rectangles:
            tim.goto(rect.x, rect.y)
            tim.pendown()
            tim.forward(rect.width * mag)
            tim.left(90)
            tim.forward(rect.height * mag)
            tim.left(90)
            tim.forward(rect.width * mag)
            tim.left(90)
            tim.forward(rect.height * mag)
            tim.left(90)
            tim.penup()
        tim.color('blue')
        for rect in list_squares:
            tim.goto(rect.x, rect.y)
            tim.pendown()
            tim.forward(rect.width * mag)
            tim.left(90)
            tim.forward(rect.height * mag)
            tim.left(90)
            tim.forward(rect.width * mag)
            tim.left(90)
            tim.forward(rect.height * mag)
            tim.left(90)
            tim.penup()
        turtle.done()
