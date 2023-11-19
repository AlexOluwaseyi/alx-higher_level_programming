#!/usr/bin/python3
"""Creates the State "California" with the City "San Francisco"
from the database hbtn_0e_100_usa
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from relationship_state import Base, State
from relationship_city import City
import sys


if __name__ == "__main__":
    # Create a SQLAlchemy engine
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    # Create all tables in the engine
    Base.metadata.create_all(engine)

    # Create a session to interact with the database
    session = Session(engine)

    # Create the State "California" and City "San Francisco"
    city = City(name="San Francisco")
    state = State(name="California")
    state.cities.append(city)

    # Add the new State to the session
    session.add_all([city, state])

    # Commit the changes to the database
    session.commit()

    # Close the session
    session.close()
