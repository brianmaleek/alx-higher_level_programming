#!/usr/bin/python3


"""
Script lists the first State objects from the database hbtn_0e_6_usa
Takes 3 arguments: mysql username, mysql password and database name
Results are sorted in ascending order by states.id
"""

from sys import argv
from model_state import State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":

    # check correct no. of command line args are provided
    if len(argv) != 4:
        print("Usage: 8-model_state_fetch_first.py <mysql_username> \
              <mysql_password> <database_name>")
        exit(1)

    # create engine to access database
    # username, password, database = argv[1], argv[2], argv[3]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(argv[1],
                                   argv[2], argv[3]), pool_pre_ping=True)

    # create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # query to fetch first State object
    first_state = session.query(State).order_by(State.id).first()

    # print first State object if it exists
    if first_state:
        print("{}: {}".format(first_state.id, first_state.name))
    else:
        print("Nothing")

    # close session
    session.close()
