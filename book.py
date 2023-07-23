import sqlite3


class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.available = True


class Library:
    def __init__(self):
        self.connection = sqlite3.connect("library.db")
        self.cursor = self.connection.cursor()
        self.create_tables()

    def create_tables(self):
        self.cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS books (
                id INTEGER PRIMARY KEY,
                title TEXT,
                author TEXT,
                available BOOLEAN
            )
            """
        )
        self.connection.commit()

    def add_book(self, title, author):
        self.cursor.execute(
            "INSERT INTO books (title, author, available) VALUES (?, ?, ?)",
            (title, author, True)
        )
        self.connection.commit()
        print(f"Book '{title}' by {author} added to the library.")
 
    def list_books(self):
        self.cursor.execute("SELECT * FROM books")
        books = self.cursor.fetchall()
        
        if not books:
            print("No books in the library.")
        else:
            print("Library Books:")
            for index, book in enumerate(books, start=1):
                status = "Available" if book[3] else "Not Available"
                print(f"{index}. '{book[1]}' by {book[2]} - {status}")

    def get_book_by_index(self, index):
        self.cursor.execute("SELECT * FROM books")
        books = self.cursor.fetchall()
        
        if 1 <= index <= len(books):
            return books[index - 1]
        return None

    def borrow_book(self, book_id):
        book = self.get_book_by_index(book_id)
        if book:
            if book[3]:
                self.cursor.execute("UPDATE books SET available = ? WHERE id = ?", (False, book[0]))
                self.connection.commit()
                print(f"You've borrowed '{book[1]}'. Enjoy reading!")
            else:
                print(f"'{book[1]}' is not available for borrowing.")
        else:
            print("Invalid book index.")

    def return_book(self, book_id):
        book = self.get_book_by_index(book_id)
        if book:
            if not book[3]:
                self.cursor.execute("UPDATE books SET available = ? WHERE id = ?", (True, book[0]))
                self.connection.commit()
                print(f"Thank you for returning '{book[1]}'.")
            else:
                print("This book is already in the library.")
        else:
            print("Invalid book index.")

    def close_connection(self):
        self.connection.close()
