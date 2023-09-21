#!/usr/bin/bash

"""
1. script creates the State “California” with the City “San Francisco”
from the database hbtn_0e_100_usa: (100-relationship_states_cities.py)
2. script takes 3 arguments: mysql username, mysql password and database name
3. use the module SQLAlchemy
4. script connects to a MySQL server running on localhost at port 3306
5. use the cities relationship for all State objects
6. code should not be executed when imported
"""

from sys import argv
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    # check correct no. of command line args are provided
    if len(argv) != 4:
        print("Usage: 100-relationship_states_cities.py <mysql_username> \
              <mysql_password> <database_name>")
        exit(1)

    # create engine to access database
    # username, password, database, state_name = argv[1], argv[2], argv[3]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(argv[1],
                                   argv[2], argv[3]), pool_pre_ping=True)

    # create all tables in database
    Base.metadata.create_all(engine)

    # create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # create a new State object
    new_state = State(name="California")

    # create a new City object
    new_city = City(name="San Francisco")

    # add new City object to new State object
    new_state.cities.append(new_city)

    # add new State object to session
    session.add(new_state, new_city)

    # commit changes to session
    session.commit()

    # close session
    session.close()
