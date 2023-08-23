# Library System

The Library System is a Python project that allows users to manage books and borrow/return them using a command-line interface. The project uses SQLite as the database to store book availability information, providing data persistence between sessions.

## Project Components

- `book.py`: Defines the `Book` class and the `Library` class for managing books and their availability.

- `member.py`: Defines the `Member` class for managing member information and book borrowing/returning.

- `member_portal.py`: Entry point for the member portal, where members can borrow and return books.

- `admin_portal.py`: Entry point for the administrators portal, where administrators can add, list, change status (borrow or return) of books.

- `main.py`: Entry point for the library management system.

## Getting Started

1. Clone this repository.

2. Install the required package (SQLite) using the following command:

    ```
    pip install pysqlite3
    ```

3. Run `main.py` to access the library management, enter "admin" to run system as an administrator, use customised name to access the member portal.

## Usage

- As an Administrator (`main.py`, enter customised name):
    - Add books to the library.
    - List available books.
    - Borrow books for members.
    - Return borrowed books.
- As a Member (`main.py`, enter `admin`):
    - Borrow available books.
    - Return borrowed books.

## Database

The project uses an SQLite database (`library.db`) to store book availability information. The database is created automatically when the project is run and is used to persist book data.
