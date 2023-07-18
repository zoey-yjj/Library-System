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


if __name__ == "__main__":
    library = Library()

    while True:
        print("\nWelcome to Library System")
        print("1. Add Book")
        print("2. List Books")
        print("0. Exit")
        choice = input("Select an option: ")

        if choice == "1":
            title = input("Enter book title: ")
            author = input("Enter author name: ")
            library.add_book(title, author)
        elif choice == "2":
            library.list_books()
        elif choice == "3":
            library.list_books()
            book_index = int(input("Enter book index to borrow: "))
            library.borrow_book(book_index)
        elif choice == "4":
            library.list_books()
            book_index = int(input("Enter book index to return: "))
            library.return_book(book_index)
        elif choice == "0":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please select a valid option.")