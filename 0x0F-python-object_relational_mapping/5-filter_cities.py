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

    with nection.cursor() as cursor:
        cursor.execute("""
            SELECT
                cities.id, cities.name
            FROM
                cities
            JOIN
                states
            ON
                cities.state_id = states.id
            WHERE
                states.name LIKE BINARY %(state_name)s
            ORDER BY
                cities.id ASC
        """, {
            'state_name': sys.argv[4]
        })
        rows = cursor.fetchall()

    if rows:
        print(", ".join([row[1] for row in rows]))
