from library_system.book import Book


def test_book_creation():

    book = Book("Python", "John", "123", 2020)

    assert book.title == "Python"
    assert book.available == True
