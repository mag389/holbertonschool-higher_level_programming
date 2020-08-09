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

    """ get the injection immune name """
    name = sys.argv[4]
    if len(name) > 15:
        exit()
    """ get the query """
    result = session.query(State).filter(State.name == name).\
        order_by(State.id).all()
    if (result):
        for state in result:
            print("{}".format(state.id))
    if len(result) is 0:
        print("Not found")
