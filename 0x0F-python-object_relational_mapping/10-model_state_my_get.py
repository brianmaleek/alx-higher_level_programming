#!/usr/bin/python3


"""
1. Script prints State object, with name passed as arguement
    from the database hbtn_0e_6_usa
2. Takes 4 arguments: mysql username, mysql password, database name
    state name to search (SQL injection free!)
3. Results must display states.id
"""

from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":

    # check correct no. of command line args are provided
    if len(argv) != 5:
        print("Usage: 10-model_state_my_get.py <mysql_username> \
              <mysql_password> <database_name> <state name>")
        exit(1)

    # create engine to access database
    # username, password, database, state_name = argv[1], argv[2], argv[3],
    #   argv[4]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(argv[1],
                                   argv[2], argv[3]), pool_pre_ping=True)

    # create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # retrieve state objects containing letter 'a' and order by state.id
    state_name = argv[4]
    sql_query = session.query(State).filter(State.name == state_name)
    result = sql_query.first()

    # print first State object if it exists
    try:
        print(result.id)
    except Exception:
        print("Not found")

    # close session
    session.close()
