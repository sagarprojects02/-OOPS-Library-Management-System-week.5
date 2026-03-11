from library_system.library import Library
from library_system.book import Book
from library_system.member import Member


def menu():

    print("\nLibrary Management System")
    print("1. Add Book")
    print("2. Register Member")
    print("3. Borrow Book")
    print("4. Return Book")
    print("5. Search Book")
    print("6. Exit")


def main():

    library = Library()

    while True:

        menu()

        choice = input("Enter choice: ")

        if choice == "1":

            title = input("Title: ")
            author = input("Author: ")
            isbn = input("ISBN: ")
            year = int(input("Year: "))

            book = Book(title, author, isbn, year)
            library.add_book(book)

        elif choice == "2":

            name = input("Member name: ")
            member_id = input("Member ID: ")

            member = Member(name, member_id)
            library.register_member(member)

        elif choice == "3":

            member_id = input("Member ID: ")
            isbn = input("Book ISBN: ")

            library.borrow_book(member_id, isbn)

        elif choice == "4":

            member_id = input("Member ID: ")
            isbn = input("Book ISBN: ")

            library.return_book(member_id, isbn)

        elif choice == "5":

            title = input("Enter title: ")
            library.search_book(title)

        elif choice == "6":
            break


if __name__ == "__main__":
    main()
