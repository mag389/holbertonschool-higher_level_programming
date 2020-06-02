#!/usr/bin/python3
""" the MY_list Class file """


class MyList(list):
    """the myList class """

    def print_sorted(self):
        """ print sorted method"""
        newlist = list(self)
        newlist.sort()
        print(newlist)
