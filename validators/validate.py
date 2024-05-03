#!/usr/bin/python3
from pydantic import BaseModel

""" Handles the validation of books data prior registration """

class Book_validator(BaseModel):
    # title must be string
    title : str
    # author must be string
    author : str
    # year must be integer
    year : int
    # isbn must be string
    isbn : str
