from library_system.member import Member
from library_system.book import Book


def test_borrow_book():

    member = Member("Rahul", "M1")
    book = Book("Python", "John", "123", 2020)

    assert member.borrow_book(book) == True
