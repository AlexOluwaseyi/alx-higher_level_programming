#!/usr/bin/python3

'''
a script that lists all states with name starting with N (upper N)
from the database hbtn_0e_0_usa
takes 3 arguments: mysql username, mysql password and database name
'''

if __name__ == "__main__":
    import MySQLdb
    from os import sys

    # Connect to the MySQL server
    db = MySQLdb.connect(
            host="localhost", port=3306,
            user=sys.argv[1], passwd=sys.argv[2],
            db=sys.argv[3]
            )

    # Get a cursor object
    cursor = db.cursor()

    # Execute the query to list all states
    cursor.execute(
            "SELECT * FROM states WHERE name \
            LIKE 'N%' ORDER BY states.id ASC"
            )

    # Fetch all the results
    results = cursor.fetchall()

    # Display the results
    for row in results:
        print(row)
