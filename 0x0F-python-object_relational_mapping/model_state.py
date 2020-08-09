#!/usr/bin/python3
""" onto the alchemy section """
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class State(Base):
    """ the state class """
    __tablename__ = 'states'
    id = Column(Integer, autoincrement=True, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)

    def __str__(self):
        """ str attr """
        return "{}".format(self.name)
