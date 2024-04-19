#!/usr/bin/python3
"""
This script lists all states from the database hbtn_0e_0_usa.
"""
import MySQLdb
import sys

if __name__ == "__main__":
    # 3 arguments
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    # connect to a MySQL server running on localhost at port 3306
    nection = MySQLdb.connect(host="localhost", port=3306,
                              user=username, passwd=password, db=db_name)

    cursor = nection.cursor()

    # sorted in ascending order by states.id
    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    rows = cursor.fetchall()

    # Display results
    for row in rows:
        print(row)

    # Close cursor and connection
    cursor.close()
    nection.close()
