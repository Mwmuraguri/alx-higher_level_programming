#!/usr/bin/python3
"""Lists all states from mySQL database"""
import sys
import MySQLdb

def liststates (username, password, database):
    """Lists all states from database hbtn_0e-0_usa,
    Args:
    username: mysql username
    password: mysql password
    database: mysql database
    """
    # connect to MYSQL server
    dbase = MySQLdb.connect(host='localhost',\
            port=3306,\
            user=username,\
            passwd=password,\
            db=database)
    cursor = dbase.cursor()

    # Execute the SQL query to grab all states
    cursor.execute("SELECT * FROM states ORDER BY id ASC")


    # Fetch all the rows
    rows = cursor.fetchall()

    # Print results
    for row in rows:
        print(row)

    # close db connection
    dbase.close()

    # Example
    if __name__ == '__main__':

        username = sys.argv[1]
        password = sys.argv[2]
        database = sys.argv[3]

        liststates(username, password, database)
