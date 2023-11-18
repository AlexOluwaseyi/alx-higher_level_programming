#!/usr/bin/python3

import MySQLdb
from os import sys

if __name__ == "__main__":
    # Connect to the MySQL server
    db = MySQLdb.connect(
            host="localhost", port=3306,
            user=sys.argv[1], passwd=sys.argv[2],
            db=sys.argv[3]
            )

    # Get a cursor object
    cursor = db.cursor()

    # Execute the query to list all states
    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    # Fetch all the results
    results = cursor.fetchall()

    # Display the results
    for row in results:
        print(row)

    # Close the cursor and connection
    cursor.close()
    db.close()
