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
    Base.metadata.create_all(engine)

    """ create session """
    Session = sessionmaker(bind=engine)
    session = Session()

    """ add california """
    new_state = State(name='California')
    session.add(new_state)
    new_city = City(name='San Francisco', state_id=1)
    new_state.cities = [new_city]
    session.add(new_city)
    session.commit()
