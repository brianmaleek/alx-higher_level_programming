#!/usr/bin/python3


"""
1. Script deletes all State objects, containing letter the
    'a' from the database hbtn_0e_6_usa
2. Takes 3 arguments: mysql username, mysql password and database name
3. Script should not be executed when imported
"""

from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":

    # check correct no. of command line args are provided
    if len(argv) != 4:
        print("Usage: 13-model_state_delete_a.py <mysql_username> \
              <mysql_password> <database_name> <state name>")
        exit(1)

    # create engine to access database
    # username, password, database, state_name = argv[1], argv[2], argv[3]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(argv[1],
                                   argv[2], argv[3]), pool_pre_ping=True)

    # create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # delete all State objects containing letter 'a'
    states_to_delete = session.query(State).filter(State.name.contains('%a'))
    if states_to_delete:
        for state in states_to_delete:
            session.delete(state)
        session.commit()
    else:
        print("No states found containing letter 'a'")

    # close session
    session.close()
