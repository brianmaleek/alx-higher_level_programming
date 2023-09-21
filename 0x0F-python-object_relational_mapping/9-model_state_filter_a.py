#!/usr/bin/python3


"""
Script lists all State objects with letter a from the database hbtn_0e_6_usa
Takes 3 arguments: mysql username, mysql password and database name
Results are sorted in ascending order by states.id
"""

from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":

    # check correct no. of command line args are provided
    if len(argv) != 4:
        print("Usage: 9-model_state_filter_a.py <mysql_username> \
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

    # retrieve state objects containing letter 'a' and order by state.id
    sql_query = session.query(State).filter(State.name.contains('%a'))
    matching_state = sql_query.order_by(State.id).all()

    # print first State object if it exists
    if matching_state:
        for state in matching_state:
            print("{}: {}".format(state.id, state.name))
    else:
        print("Nothing")

    # close session
    session.close()
