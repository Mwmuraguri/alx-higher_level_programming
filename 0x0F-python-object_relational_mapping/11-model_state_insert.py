#!/usr/bin/python3
"""Adds a new state to a MySQL database using SQLAlchemy."""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State

if __name__ == "__main__":
    # Create the SQLAlchemy engine using the provided MySQL credentials
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    # Create a session factory
    Session = sessionmaker(bind=engine)

    # Creating a session object
    session = Session()

    # Creating a new State object for Louisiana
    louisiana = State(name="Louisiana")
    # Adding the new state to the session
    session.add(louisiana)
    # Commit the session
    session.commit()
    # Print the ID
    print(louisiana.id)

