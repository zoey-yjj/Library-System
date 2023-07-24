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
                book = self.library.get_book_by_title_author(title, author)
                if book:
                    member.borrow_book(book)
                else:
                    print("Book not found.")
            # return book
            elif choice == "2":
                title = input("Enter book title to return: ")
                author = input("Enter book author: ")
                book = self.library.get_book_by_title_author(title, author)
                if book:
                    member.return_book(book)
                else:
                    print("Book not found.")
            # exit from the system
            elif choice == "0":
                print("Exiting...")
                break
            else:
                print("Invalid choice. Please select a valid option.")
