#!/usr/bin/python3


"""
1. Script adds the State "Louisiana" to the database hbtn_0e_6_usa
2. Takes 3 arguments: mysql username, mysql password and database name
3. print the new states.id after creation
4. Script should not be executed when imported
"""

from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":

    # check correct no. of command line args are provided
    if len(argv) != 4:
        print("Usage: 9-model_state_filter_a.py <mysql_username> \
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

    # Add the State "Louisiana" to the database
    new_state = State(name="Louisiana")
    session.add(new_state)
    session.commit()

    # print new state
    print(new_state.id)

    # close session
    session.close()
