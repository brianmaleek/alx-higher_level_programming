#!/usr/bin/python3

"""
1. Script takes in an argument and displays all values
    in states table of hbtn_0e_0_usa where name matches
    the argument. write one that is safe from MySQL injections!
2. Takes 4 arguments: mysql username, mysql password,
database name and state name searched
3. Format creates SQL Query with user input.
4. Results are sorted in ascending order by states.id
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
    sql_query = "SELECT * FROM states WHERE name = %s\
                ORDER BY id ASC"
    cursor.execute(sql_query, (argv[4],))
    states = cursor.fetchall()

    for state in states:
        print(state)

    # disconnect from server
    cursor.close()
    db.close()
