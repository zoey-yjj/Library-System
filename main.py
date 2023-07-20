from book import Library
from member import Member


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