import json
from .book import Book
from .member import Member


class Library:

    def __init__(self):
        self.books = {}
        self.members = {}

    def add_book(self, book):
        self.books[book.isbn] = book
        print("Book added successfully")

    def register_member(self, member):
        self.members[member.member_id] = member
        print("Member registered successfully")

    def find_book(self, isbn):
        return self.books.get(isbn)

    def borrow_book(self, member_id, isbn):

        member = self.members.get(member_id)
        book = self.books.get(isbn)

        if member and book and book.available:

            if member.borrow_book(book):
                book.check_out()
                print("Book borrowed successfully")
            else:
                print("Borrow limit reached")
        else:
            print("Book or member not found")

    def return_book(self, member_id, isbn):

        member = self.members.get(member_id)
        book = self.books.get(isbn)

        if member and book:
            member.return_book(book)
            book.return_book()
            print("Book returned successfully")

    def search_book(self, title):

        for book in self.books.values():
            if title.lower() in book.title.lower():
                print(book)

    def save_books(self):

        data = [book.to_dict() for book in self.books.values()]

        with open("data/books.json", "w") as f:
            json.dump(data, f, indent=4)

    def load_books(self):

        try:
            with open("data/books.json") as f:
                data = json.load(f)

            for item in data:
                book = Book(
                    item["title"],
                    item["author"],
                    item["isbn"],
                    item["year"]
                )
                book.available = item["available"]
                self.books[book.isbn] = book

        except FileNotFoundError:
            pass
