#!/usr/bin/python3
"""Lists all State objects that contain the letter a from
the database hbtn_0e_6_usa
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model_state import Base, State
import sys

if __name__ == "__main__":
    # Create a SQLAlchemy engine
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    # State name to filter in query
    stateName = sys.argv[4]

    # Create all tables in the engine
    Base.metadata.create_all(engine)

    # Create a session to interact with the database
    session = Session(engine)

    # Query and print all State objects containing the letter 'a', sorted by id
    state_by_name = session.query(State).filter(State.name
                                                == stateName).first()

    if state_by_name:
        print("{}".format(state_by_name.id))
    else:
        print("Not found")

    # Close the session
    session.close()
