import sqlite3


class Member:
    def __init__(self, name):
        self.name = name
        self.borrowed_books = []

    def borrow_book(self, book):
        if book[3]:
            connection = sqlite3.connect("library.db")
            cursor = connection.cursor()
            cursor.execute("UPDATE books SET available = ? WHERE id = ?", (False, book[0]))
            connection.commit()
            connection.close()
            print(f"{self.name} has borrowed '{book[1]}'.")
        else:
            print(f"'{book[1]}' is not available for borrowing.")

    def return_book(self, book):
        if not book[3]:
            connection = sqlite3.connect("library.db")
            cursor = connection.cursor()
            cursor.execute("UPDATE books SET available = ? WHERE id = ?", (True, book[0]))
            connection.commit()
            connection.close()
            print(f"{self.name} has returned '{book[1]}'.")
        else:
            print(f"{self.name}, '{book[1]}' is already in the library.")
