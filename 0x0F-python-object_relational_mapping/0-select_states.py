#!/usr/bin/python3

"""
Script lists all states from the database hbtn_0e_0_usa
Takes 3 arguments: mysql username, mysql password and database name
Results are sorted in ascending order by states.id
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
    cursor.execute("SELECT * FROM states ORDER BY id ASC")
    states = cursor.fetchall()

    for state in states:
        print(state)

    # disconnect from server
    cursor.close()
    db.close()
