class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.available = True


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, title, author):
        book = Book(title, author)
        self.books.append(book)
        print(f"Book '{title}' by {author} added to the library.")
    
    def list_books(self):
        if not self.books:
            print("No books in the library.")
        else:
            print("Library Books:")
            for index, book in enumerate(self.books, start=1):
                status = "Available" if book.available else "Not Available"
                print(f"{index}. '{book.title}' by {book.author} - {status}")

    def borrow_book(self, book_index):
        if 1 <= book_index <= len(self.books):
            book = self.books[book_index - 1]
            if book.available:
                book.available = False
                print(f"You've borrowed '{book.title}'. Enjoy reading!")
            else:
                print(f"'{book.title}' is not available for borrowing.")
        else:
            print("Invalid book index.")

    def return_book(self, book_index):
        if 1 <= book_index <= len(self.books):
            book = self.books[book_index - 1]
            if not book.available:
                book.available = True
                print(f"Thank you for returning '{book.title}'.")
            else:
                print("This book is already in the library.")
        else:
            print("Invalid book index.")

