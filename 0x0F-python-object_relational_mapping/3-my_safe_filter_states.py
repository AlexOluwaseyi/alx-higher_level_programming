#!/usr/bin/python3

'''
Same script, but better - Prevent/avoid SQL Injection

a script that takes in an argument and displays all values in the
states table of hbtn_0e_0_usa where name matches the argument.

takes 4 arguments: mysql username, mysql password,
database name and state name
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

    # The name of the state to be queried
    stateName = db.escape_string(sys.argv[4]).decode()

    # Get a cursor object
    cursor = db.cursor()

    # Execute the query to list all states with same
    cursor.execute(
            "SELECT * FROM states WHERE name \
            LIKE '{}' ORDER BY states.id ASC;".format(stateName)
            )

    # Fetch all the results
    results = cursor.fetchall()

    # Display the results
    for row in results:
        print(row)

    # Close the cursor and connection
    cursor.close()
    db.close()
