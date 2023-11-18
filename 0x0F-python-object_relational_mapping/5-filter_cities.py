#!/usr/bin/python3

'''
a script that lists all states from the database hbtn_0e_0_usa
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
