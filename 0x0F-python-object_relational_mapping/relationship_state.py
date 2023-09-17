#!/usr/bin/python3
"""Module that defines a state model that contain the class definition
 of a State and an instance Base = declarative_base()
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """
    inherits from Base Tips
    links to the MySQL table states
    class attribute id that represents a column
     of an auto-generated, unique integer,
    """
    __tablename__ = "states"
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
