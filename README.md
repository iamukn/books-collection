## Book Management API with FastAPI and SQLAlchemy

This project is a simple CRUD (Create, Read, Update, Delete) application built using FastAPI and SQLAlchemy. It manages a database of books and provides endpoints to perform CRUD operations on the book collection.

### Requirements

- **Framework**: FastAPI for building the API.
- **Database**: SQLAlchemy for ORM.
- **Functionality**: Implement CRUD operations for managing a collection of books.
- **Data Model**: Each book should have the following attributes:
  - id (integer, auto-generated)
  - title (string)
  - author (string)
  - year (integer)
  - isbn (string)
- **Endpoints**:
  - `GET /books`: Retrieve a list of all books.
  - `GET /books/{id}`: Retrieve information about a specific book.
  - `POST /books`: Add a new book to the collection.
  - `PUT /books/{id}`: Update information about a specific book.
  - `DELETE /books/{id}`: Delete a book from the collection.
- **Input Validation**:
  - Ensure that required fields are provided (title, author, year, isbn).
  - Validate input types and formats (e.g., year should be an integer, isbn should be a string).
- **Environment Variable**:
  - Set an environment variable called `PATH` that holds the path to the SQLite3 file.
- **Initialization**:
  - Run `python3 models.py` to create the table in the database.
- **Dependencies Installation**:
  - Run `pip install -r requirements.txt` to install the required dependencies.

### Getting Started

1. Clone this repository:

   ```bash
   git clone https://github.com/your-username/book-management-api.git
   ```

2. Navigate to the root directory:


3. Set the environment variable `PATH`:

   ```bash
   export path=sqlite:///./test.db
   ```

4. Run `python3 models.py` to create the table in the database.

5. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

6. Run the application:

   ```bash
   uvicorn app:app --reload
   ```

7. Access the SWAGGERAPI documentation in your browser:

   ```
   http://localhost:8000/docs
   ```

### Usage

- Use the provided endpoints to perform CRUD operations on the book collection.
- Ensure to provide required fields and valid input formats when adding or updating books.
- Explore the Swagger documentation for detailed information on available endpoints and request/response formats.
