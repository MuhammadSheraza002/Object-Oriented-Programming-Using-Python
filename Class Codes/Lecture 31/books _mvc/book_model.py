from book import *
class Book_Model:
    def __init__(self):
        self.books = []

    def add_book(self, title, price):
        self.books.append(Book(title, price))

    def get_books(self):
        return self.books

    def get_book(self, book_no):
        for book in self.books:
            if book.get_book_no() == book_no:
                return book

    def get_book_by_title(self, title):
        for book in self.books:
            if book.get_title() == title:
                return book

    def update_book(self, book_no, title, price):
        for book in self.books:
            if book.get_book_no() == book_no:
                book.set_title(title)
                book.set_price(price)

    def delete_book(self, book_no):
        for book in self.books:
            if book.get_book_no() == book_no:
                self.books.remove(book)
