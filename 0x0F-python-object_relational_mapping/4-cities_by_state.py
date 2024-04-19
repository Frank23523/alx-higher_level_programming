#!/usr/bin/python3
"""
lists all cities from the database hbtn_0e_4_usa
"""

import MySQLdb
import sys

if __name__ == '__main__':
    """
    4 arguments,
    connected to MySQL server running on localhost at port 3306
    """
    nection = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3]
            )
    cursor = nection.cursor()
    cursor.execute("SELECT cities.id, cities.name, states.name \
            FROM cities \
            JOIN states ON cities.state_id = states.id \
            ORDER BY cities.id ASC")
    rows = cursor.fetchall()

    for row in rows:
        print(row)
