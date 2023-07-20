from book import Library


class Admin_Portal:
    def __init__(self):
        self.library = Library()

    def execute(self):
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
                self.library.add_book(title, author)
            elif choice == "2":
                self.library.list_books()
            elif choice == "3":
                self.library.list_books()
                book_index = int(input("Enter book index to borrow: "))
                self.library.borrow_book(book_index)
            elif choice == "4":
                self.library.list_books()
                book_index = int(input("Enter book index to return: "))
                self.library.return_book(book_index)
            elif choice == "0":
                print("Exiting...")
                break
            else:
                print("Invalid choice. Please select a valid option.")
