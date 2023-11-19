#!/usr/bin/python3
"""
Improve the files model_city.py and model_state.py, and save
them as relationship_city.py and relationship_state.py
"""
import sys
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from relationship_state import State, Base
from relationship_city import City


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    session = Session(engine)
    new_state = State(name='California')
    new_city = City(name='San Francisco')
    new_state.cities.append(new_city)
    session.add_all([new_state, new_city])
    session.commit()
    session.close()
