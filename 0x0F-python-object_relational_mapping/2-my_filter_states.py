#!/usr/bin/python3
"""
This script takes in an argument and
displays all values in the states
where `name` matches the argument
from the database `hbtn_0e_0_usa`.
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

    cursor.execute(
        "SELECT * FROM states WHERE name LIKE BINARY '{}' ORDER BY \
                        states.id ASC".format(sys.argv[4]))
    rows = cursor.fetchall()

    for row in rows:
        print(row)
