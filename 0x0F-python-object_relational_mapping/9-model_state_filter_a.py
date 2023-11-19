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

    # Create all tables in the engine
    Base.metadata.create_all(engine)

    # Create a session to interact with the database
    session = Session(engine)

    # Query and print all State objects containing the letter 'a', sorted by id
    states_with_a = session.query(State).filter(State.name.like('%a%'))\
        .order_by(State.id).all()

    for state in states_with_a:
        print("{}: {}".format(state.id, state.name))

    # Close the session
    session.close()
