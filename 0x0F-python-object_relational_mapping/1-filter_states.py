#!/usr/bin/python3

"""
1. Script lists all states with a name starting with
'N' (upper N) from the database hbtn_0e_0_usa
2. Takes 3 arguments: mysql username, mysql password and database name
3. Results are sorted in ascending order by states.id
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
    sql_name = "SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC"
    cursor.execute(sql_name)
    states = cursor.fetchall()

    for state in states:
        if state[1][0] == 'N':
            print(state)

    # disconnect from server
    cursor.close()
    db.close()
