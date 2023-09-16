#!/usr/bin/python3
"""Lists all states from the hbtn_0e_0_usa database."""
import sys
import MySQLdb

if __name__ == "__main__":
    import MySQLdb
    import sys

    # Getting the command-line arg
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]
    state_name = sys.argv[4]

    # Connecting to the MySQL server
    db = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=mysql_username,
        passwd=mysql_password,
        db=database_name
    )
    # Creating a cursor object to execute queries
    cursor = db.cursor()

    # Preparingg the SQL query with placeholders
    sql_query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"

    # Executing the query with the state name
    cursor.execute(sql_query, (state_name,))

    # Fetching all the rows returned by query
    rows = cursor.fetchall()

    # Display the results
    for row in rows:
        print(row)

    # Close the cursor and database connection
    cursor.close()
    db.close()

