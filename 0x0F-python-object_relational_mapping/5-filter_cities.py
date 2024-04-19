#!/usr/bin/python3
"""
This script takes in the name of a state as an argument
and lists all cities of that state,
using the database hbtn_0e_4_usa
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
    query = """
    SELECT GROUP_CONTACT(cities.name SEPARATOR ', ')
    FROM cities
    JOIN states ON cities.state_id = states.id
    WHERE states.name = %s
    """
    cursor.execute(query, (state_name,))
    result = cursor.fetchone()[0]

    if display:
        print(result)
    else:
        print("")
