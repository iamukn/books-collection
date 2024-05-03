#!/usr/bin/python3
from fastapi import APIRouter, HTTPException, Response
from models.models import Books
from models.crud_operation import CRUD_operation as CRUD
from validators.validate import Book_validator
from json import dumps
""" handles the /books endpoint with post and get methods"""

get_create_router = APIRouter()

# create a CRUD object
crud = CRUD()

# create simple root route
@get_create_router.get('/books')
async def retrieve_books():
    global crud
    books = crud.retrieve_all()
    return {'books': books}

# fetches books from the database using its unique id
@get_create_router.post('/books')
async def create_a_book(book: Book_validator):
    global crud
    book = book.dict() 
    data = crud.create_one(book)
    return Response(status_code=201)
