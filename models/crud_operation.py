#!/usr/bin/python3
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .models import Books
from os import getenv

# gets the path to the database file
PATH = getenv("path")
# create a database engine
engine = create_engine(PATH, echo=False)
Session = sessionmaker(bind=engine)
session = Session()

class CRUD_operation:
    
    # method that returns all the books from the database
    def retrieve_all(self):
        # returns all the books from the database
        return session.query(Books).all()

    def create_one(self, book_info):
        try:
            # creates a new book in the database
            book = Books(**book_info)
            session.add(book)
            session.commit()
            session.close()
            return book
        except Exception as e:
            return e

    def retrieve_one(self, id):
        # fetch the book from the database for a user
        try:
            book = session.query(Books).filter_by(id=id).first()
            return book
        except Exceotion as e:
            return e

    def update(self, id, book_info):
        if not id or not book_info:
            return 'An issue occured, check submitted data'

        # fetch the book from the database and update
        try:
            book = session.query(Books).filter_by(id=id).first()
            
            if book:
                # make modification to the book if it exist
                book.title = book_info.title
                book.author = book_info.author
                book.year = book_info.year
                book.isbn = book_info.isbn
                session.commit()
                session.close()
                # return the book
            return book
        # returns an error if an exception is raised
        except Exception as e:
            return e

    def delete(self, id):
        # deletes a book
        if not id:
            # ensures an id is passed
            return 'An id is required!'
        # checks to see if a book exists with the id
        book = session.query(Books).filter_by(id=id).first()
        if book:
            # delete if it exist
            session.delete(book)
            return "Deleted successfully"
        # return an empty list if it doesn't exist
        return book
