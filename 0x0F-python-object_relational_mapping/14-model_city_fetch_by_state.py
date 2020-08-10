#!/usr/bin/python3
""" script to get all cities with their states """
from model_state import Base, State
from model_city import City
from sqlalchemy.orm import sessionmaker
from sqlalchemy import (create_engine)
import sys


if __name__ == "__main__":
    """ creat the engine """
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
             sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)

    """ create session """
    Session = sessionmaker(bind=engine)
    session = Session()

    """ query the right stuff """
    for s, c in session.query(State, City).\
            filter(State.id == City.state_id):
        print(s.name, ": (", c.id, ") ", c.name, sep="")
