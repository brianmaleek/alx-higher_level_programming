#!/usr/bin/python3

"""
1. Script lists all State objects from the database hbtn_0e_6_usa
2. Import State and Base from model_state - from model_state import Base, State
3. Results are sorted in ascending order by states.id
"""

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    # Create engine that connects to the core (MySQL)
    username, password, database = argv[1], argv[2], argv[3]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        username, password, database), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    """
    setting up a session
    """
    Session = sessionmaker(bind=engine)
    session = Session()

    """
    fetching data
    """
    state_data = session.query(State).order_by(State.id).all()

    for state in state_data:
        print("{}: {}".format(state.id, state.name))

    session.close()
