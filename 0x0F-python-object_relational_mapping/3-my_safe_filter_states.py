#!/usr/bin/python3
"""
Like 2-my_filter_states.py but this script is safe from MySQL injections!
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
        "SELECT * FROM states WHERE name LIKE BINARY %(name)s ORDER BY \
                states.id ASC", {'name': sys.argv[4]})
    rows = cursor.fetchall()

    for row in rows:
        print(row)
