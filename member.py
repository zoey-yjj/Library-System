class Member:
    def __init__(self, name):
        self.name = name
        self.borrowed_books = []

    def borrow_book(self, book):
        if book.available:
            self.borrowed_books.append(book)
            book.available = False
            print(f"{self.name} has borrowed '{book.title}'.")
        else:
            print(f"'{book.title}' is not available for borrowing.")

    def return_book(self, book):
        if not book.available:
            self.borrowed_books.remove(book)
            book.available = True
            print(f"{self.name} has returned '{book.title}'.")
        else:
            print(f"{self.name}, '{book.title}' is already in the library.")

