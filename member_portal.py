from member import Member
from book import Library


class Member_Portal:
    def __init__(self, name):
        self.member = Member(name)
        self.library = Library()
    
    def execute(self):
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
                for book in self.library.books:
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
                for book in self.library.books:
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
