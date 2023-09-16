#!/usr/bin/python3

"""Lists all states from the hbtn_0e_0_usa database."""

import sys
import MySQLdb

if __name__ == "__main__":

    # Getting MySQL credentials and search name from command-line
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    c = db.cursor()

    # Executing the SQL query to retrieve states
    c.execute("SELECT * \
                 FROM `states` \
                WHERE BINARY `name` = '{}'".format(sys.argv[4]))

    # Fetching all the rows and print the states
    [print(state) for state in c.fetchall()]

