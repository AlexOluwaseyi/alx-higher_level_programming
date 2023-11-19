#!/usr/bin/python3

"""
a script that takes in an argument and displays all values in the
states table of hbtn_0e_0_usa where name matches the argument.

takes 4 arguments: mysql username, mysql password,
database name and state name
"""

import MySQLdb
import sys


def search_states(username, password, database, search_name):
    # Connect to the MySQL server
    db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            passwd=password,
            db=database
            )

    # Create a cursor object to interact with the database
    cursor = db.cursor()

    # Execute the SQL query to retrieve states matching the input name
    query = """SELECT * FROM states WHERE name LIKE BINARY '{}'
            ORDER BY states.id ASC"""
    cursor.execute(query, (state_name,))

    # Fetch all the rows
    states = cursor.fetchall()

    # Display the results
    for state in states:
        print(state)

    # Close the cursor and connection
    cursor.close()
    db.close()


if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: {} <username> <password> <database> \
                <state_name>".format(sys.argv[0]))
        sys.exit(1)

    username, password, database, state_name \
        = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]
    search_states(username, password, database, state_name)
