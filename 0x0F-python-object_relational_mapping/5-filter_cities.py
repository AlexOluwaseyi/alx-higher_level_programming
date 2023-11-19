#!/usr/bin/python3

'''
a script that takes in the name of a state as an argument
and lists all cities of that state
take 4 arguments: mysql username, mysql password, database
name and state name (SQL injection free!)
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

    # State name from command argument
    stateName = db.escape_string(sys.argv[3])

    # Get a cursor object
    cursor = db.cursor()

    # Execute the query to list all states
    cursor.execute("SELECT cities.name FROM cities JOIN states \
            ON states.id = cities.state_id WHERE states.name = '{}' \
            ORDER BY cities.id ASC".format(sys.argv[4]))

    # Fetch all the results
    results = cursor.fetchall()

    # Display the results
    print(", ".join(row[0] for row in results))

    # Close the cursor and connection
    cursor.close()
    db.close()
