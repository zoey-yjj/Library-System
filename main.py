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


if __name__ == "__main__":
    library = Library()

    member_name = input("Enter member name: ")

    # normal member
    if member_name != 'admin':
        while True:
            print("\nMember Portal")
            print("1. Borrow Book")
            print("2. Return Book")
            print("0. Exit")
            choice = input("Select an option: ")
            # borrow book
            if choice == "1":
                title = input("Enter book title to borrow: ")
                author = input("Enter book author: ")
                book_to_borrow = None
                # check if the book exist in the library
                for book in library.books:
                    if book.title == title and book.author == author:
                        book_to_borrow = book
                        break

                if book_to_borrow:
                    member.borrow_book(book_to_borrow)
                else:
                    print("Book not found.")
            # return book
            elif choice == "2":
                title = input("Enter book title to return: ")
                author = input("Enter book author: ")
                book_to_return = None
                # check if the book exist in the library
                for book in library.books:
                    if book.title == title and book.author == author:
                        book_to_return = book
                        break

                if book_to_return:
                    member.return_book(book_to_return)
                else:
                    print("Book not found.")
            # exit from the system
            elif choice == "0":
                print("Exiting...")
                break
            else:
                print("Invalid choice. Please select a valid option.")

    else:
        while True:
            print("\nWelcome to Library System")
            print("1. Add Book")
            print("2. List Books")
            print("3. Borrow Book")
            print("4. Return Book")
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