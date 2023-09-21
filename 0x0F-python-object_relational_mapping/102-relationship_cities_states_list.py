#!/usr/bin/python3

"""
1. script lists all City objects from the database hbtn_0e_101_usa
2. script takes 3 arguments: mysql username, mysql password and database name
3. use the module SQLAlchemy
4. script connects to a MySQL server running on localhost at port 3306
5. use state relationship to access the State object linked to the City object
6. Results sorted in ascending order by cities.id
7. code should not be executed when imported
"""

from sys import argv
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    # check correct no. of command line args are provided
    if len(argv) != 4:
        print("Usage: 102-relationship_cities_states_list.py <mysql_username> \
              <mysql_password> <database_name>")
        exit(1)

    # create engine to access database
    # username, password, database, state_name = argv[1], argv[2], argv[3]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(argv[1],
                                   argv[2], argv[3]), pool_pre_ping=True)

    # create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # query all City objects and associated state objects
    cities_with_states = session.query(City).order_by(City.id).all()

    # print each city and their corresponding state
    for city in cities_with_states:
        print("{}: {} -> {}".format(city.id, city.name, city.state.name))

    # close session
    session.close()
