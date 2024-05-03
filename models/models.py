#!/usr/bin/python3
""" Creates a book table using sqlite3 as the db """

from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from os import getenv

# gets the path to the database file
PATH = getenv("path")
# create a database engine
engine = create_engine(PATH, echo=False)

# creates a Base class for table creation
Base = declarative_base()

# create a Book table
class Books(Base):
    __tablename__ = "books"
    id = Column(Integer, primary_key =True, nullable=False)
    title = Column(String(255), nullable=False)
    author = Column(String(255), nullable=False)
    year = Column(Integer, nullable=False)
    isbn = Column(String(255), nullable=False)

    def __repr__(self):
        return '%s, %i '%(self.title, self.year)

# creates a table in the database
Base.metadata.create_all(engine)
