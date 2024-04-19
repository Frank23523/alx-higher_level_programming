#!/usr/bin/python3
"""
This script lists all states with a name starting with N (upper N)
"""


import sys
import MySQLdb


if __name__ == "__main__":
    # Connect to MySQL server
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cursor = db.cursor()

    # Execute the SQL query to retrieve all states sorted by id
    cursor.execute("SELECT * FROM `states` ORDER BY `id`")
    [print(state) for state in cursor.fetchall() if state[1][0] == "N"]
