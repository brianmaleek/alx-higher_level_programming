#!/usr/bin/python3


"""
1. Script prints all cityfrom the database hbtn_0e_14_usa
2. Takes 3 arguments: mysql username, mysql password and database name
3. results must be sorted in ascending order by citie.id
4. Results must be display as they are in the example below
    (<state name>: (<city id>) <city name>)
5. Script should not be executed when imported
"""

from sys import argv
from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":

    # check correct no. of command line args are provided
    if len(argv) != 4:
        print("Usage: 14-model_city_fetch_by_state.py <mysql_username> \
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

    # Query and retrieve City objects, sorted by cities.id
    cities = session.query(City).order_by(City.id).all()

    # Print the City objects
    for city in cities:
        state_name_query = session.query(State).filter_by(id=city.state_id)
        result = state_name_query.first().name
        print(f"{result}: ({city.id}) {city.name}")

    # close session
    session.close()
