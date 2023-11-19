#!/usr/bin/python3

'''
a script 14-model_city_fetch_by_state.py that prints all
City objects from the database hbtn_0e_14_usa

take 3 arguments: mysql username, mysql password and database name
'''

from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model_state import Base, State
from model_city import City
import sys


if __name__ == "__main__":
    # Create a SQLAlchemy engine
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    Base.metadata.create_all(engine)

    # Create a session to interact with the database
    session = Session(engine)

    # Query and print all City objects, sorted by id
    cities_states = session.query(City, State).filter(
        City.state_id == State.id).order_by(City.id).all()

    for city, state in cities_states:
        print("{}: ({}) {}".format(state.name, city.id, city.name))

    # Close the session
    session.close()
