#!/usr/bin/python3
""" script to get all cities with their states """
from relationship_state import Base, State
from relationship_city import City
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

    """ queries """
    for state in session.query(State).order_by(State.id):
        print(state.id, ": ", state.name, sep="")
        for stat, city in session.query(State, City).\
                filter(State.id == City.state_id).\
                filter(City.state_id == state.id).order_by(City.id):
            print("    ", city.id, ": ", city.name, sep="")
