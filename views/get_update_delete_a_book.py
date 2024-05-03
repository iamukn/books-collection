#!/usr/bin/python3
from fastapi import APIRouter, HTTPException, Response
from validators.validate import Book_validator
from models.crud_operation import CRUD_operation as CRUD
from json import dumps
""" Handles GET, PUT and DELETE request for a unique id """

router2 = APIRouter()

# create a CRUD object
crud = CRUD()

# fetches books from the database using its unique id
@router2.get('/books/{id}')
async def get_items(id: int):
    global crud
    # fetches a book using its id
    book = crud.retrieve_one(id)
    if not book:
        raise HTTPException(status_code=404, detail='Found no book with id %i'%id)
    # returns the book if found in the database
    return book

# updates the resource of a book
@router2.put('/books/{id}')
async def update_item(id: int, book_data: Book_validator):
    global crud
    # fetches a book using the id
    book = crud.update(id, book_data)
    # checks if the book doesn't exist
    if not book:
        # raises  an exception with an error message if not found
        raise HTTPException(status_code=404, detail='Found no book with id %i'%id)
    # updates the book with the new data
    # return the updated book
    return book

@router2.delete('/books/{id}')
async def delete_item(id: int):
    global crud
    data = crud.delete(id)
    if data:
        data = dumps({"details":data}).encode('utf-8')
        response = Response(status_code=204, content=data, media_type="application/json")
        response.headers['Content-Length'] = str(len(data))
        return response
    # raises an exception 
    raise HTTPException(status_code=404, detail='Found no book with id %i'%id)
