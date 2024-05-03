#!/usr/bin/python3
""" Basic fastapi project"""

from fastapi import FastAPI, HTTPException
from typing import Union, Any
import uvicorn
#from validators.validate import Book
from views.retrieve_create import get_create_router as router1
from views.get_update_delete_a_book import router2

app = FastAPI()

app.include_router(router1)
app.include_router(router2)

# dunder that starts the server is this script is executed directly and not imported
if __name__ == "__main__":
    uvicorn.run(app, host='0.0.0.0', port=8000,)
