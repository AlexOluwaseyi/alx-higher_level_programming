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
    query = """
    SELECT cities.name AS city_name
    FROM cities
    JOIN states
    ON cities.state_id = states.id
    WHERE states.name = %s
    ORDER BY cities.id ASC
    """

    cursor.execute(query, (stateName,))

    # Fetch all the results
    results = [row[0] for row in cursor.fetchall()]

    # Display the results
    print(", ".join(results))

    # Close the cursor and connection
    cursor.close()
    db.close()
