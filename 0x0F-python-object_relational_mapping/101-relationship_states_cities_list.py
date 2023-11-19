#!/usr/bin/python3
"""Lists all State objects and corresponding City objects
from the database hbtn_0e_101_usa
"""

import sys
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy.schema import Table


if __name__ == "__main__":
    # Create a SQLAlchemy engine
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    # Create all tables in the engine
    Base.metadata.create_all(engine)

    # Create a session to interact with the database
    session = Session(engine)

    # Query all State objects and their corresponding City objects
    states_with_cities = session.query(State).order_by(State.id).all()

    # Print the results
    for state in states_with_cities:
        print("{}: {}".format(state.id, state.name))
        for city in state.cities:
            print("    {}: {}".format(city.id, city.name))

    # Close the session
    session.close()
