#!/usr/bin/python3
""" gets all state with alchemy """
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import (create_engine)
import sys


if __name__ == "__main__":
    """ create the engine """
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
             sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)

    """ create the session """
    Session = sessionmaker(bind=engine)
    session = Session()

    """ create new state and add it """
    louis = State(name='Louisiana')
    session.add(louis)
    new_state = session.query(State).filter_by(name='Louisiana').first()
    session.commit()
    print(new_state.id)
