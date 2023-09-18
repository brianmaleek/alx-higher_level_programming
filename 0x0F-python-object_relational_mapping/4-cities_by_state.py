#!/usr/bin/python3

"""
1. Script lists all cities from the database hbtn_0e_4_usa
2. Takes 3 arguments: mysql username, mysql password, and
database name
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
    sql_query = "SELECT cities.id, cities.name, states.name\
                FROM states JOIN cities ON states.id = cities.states_id\
                ORDER BY cities.id ASC"
    cursor.execute(sql_query)
    states = cursor.fetchall()

    for state in states:
        print(state)

    # disconnect from server
    cursor.close()
    db.close()
