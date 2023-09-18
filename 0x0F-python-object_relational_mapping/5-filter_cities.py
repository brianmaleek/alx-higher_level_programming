#!/usr/bin/python3

"""
1. Script takes a name of a state as an argument
    and lists all cities of that state. database used hbtn_0e_4_usa
2. Takes 4 arguments: mysql username, mysql password,
database name and state name (SQL injection free!)
3. Results are sorted in ascending order by states.id
4. You can use the execute method only once
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":

    # Open database connection
    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=argv[1],
                         passwd=argv[2],
                         db=argv[3])

    # prepare a cursor object using cursor() method
    cursor = db.cursor()

    # Define the SQL query to be executed
    sql_query = "SELECT cities.name FROM cities\
                JOIN states ON cities.state_id = state.id\
                WHERE states.name LIKE %s\
                ORDER BY cities.id ASC"

    cursor.execute(sql_query, (argv[4], ))
    cities = cursor.fetchall()

    # format the printing of cities of same state separated by commas
    city_names = [city[0] for city in cities]
    print(', '.join(city_names))

    # disconnect from server
    cursor.close()
    db.close()
