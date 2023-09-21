#!/usr/bin/python3


"""
1. Script changes the name of a State from the database hbtn_0e_6_usa
2. Takes 3 arguments: mysql username, mysql password and database name
3. change the name of the State where id = 2 to New Mexico
4. Script should not be executed when imported
"""

from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":

    # check correct no. of command line args are provided
    if len(argv) != 4:
        print("Usage: 12-model_state_update_id_2.py <mysql_username> \
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

    # change the name of the State where id = 2 to New Mexico
    state_to_update = session.query(State).filter(State.id == 2).first()
    if state_to_update:
        state_to_update.name = "New Mexico"
        session.commit()
    else:
        print("State with id == 2 not found")

    # close session
    session.close()
