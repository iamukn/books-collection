#!/usr/bin/python3
""" Basic fastapi project"""

from fastapi import FastAPI, HTTPException
import uvicorn
from views.retrieve_create import get_create_router as router1
from views.get_update_delete_a_book import router2

# created an instance of the FastAPI class
app = FastAPI()

# registered the routes
app.include_router(router1)
app.include_router(router2)

# dunder that starts the server if this script is executed directly and not imported
if __name__ == "__main__":
    uvicorn.run(app, host='0.0.0.0', port=8000,)
