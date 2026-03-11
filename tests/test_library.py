from library_system.library import Library
from library_system.book import Book
from library_system.member import Member


def test_add_book():

    library = Library()
    book = Book("Python", "John", "123", 2020)

    library.add_book(book)

    assert "123" in library.books
