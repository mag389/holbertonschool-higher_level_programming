#!/usr/bin/python3
"""file for sinlgy linked lists """


class Node:
    """" Node class for linked lists"""

    def __init__(self, data, next_node=None):
        """initializer for node"""
        self.sdata(data)
        self.snext_node(next_node)

    def gdata(self):
        """ getter for data"""
        return self.__data

    def sdata(self, value):
        """setter for data"""
        if type(value) is not int:
            raise TypeError("data must be an integer")
        self.__data = value

    def gnext_node(self):
        """getter for next node"""
        return self.__next_node

    def snext_node(self, value):
        "setter for next node"
        if type(value) is not Node and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """ the linked list class """

    def __init__(self):
        """ initializr for linked list"""
        self.__head = None
        pass

    def sorted_insert(self, value):
        """ insert new node"""
        if self.__head is None:
            self.__head = Node(value)
        elif (self.__head).gdata() > value:
                self.__head = Node(value, self.__head)
        else:
            temp = self.__head
            while temp is not None:
                if temp.gnext_node() is None:
                    temp.snext_node(Node(value))
                    break
                if (temp.gnext_node()).gdata() < value:
                    temp = temp.gnext_node()
                else:
                    temp.snext_node(Node(value, temp.gnext_node()))
                    break

    def __str__(self):
        retstr = ""
        temp = self.__head
        while temp is not None:
            retstr = retstr + str(temp.gdata())
            temp = temp.gnext_node()
            if temp is not None:
                retstr = retstr + "\n"
        return retstr
