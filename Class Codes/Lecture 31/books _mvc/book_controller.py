from book import *
from book_view import *
from book_model import *

class Book_Controller:
    def __init__(self, book_model, book_view):
        self.book_model = book_model
        self.book_view = book_view

    def show_books(self):
        self.book_view.show_books(self.book_model.get_books())

    def show_book(self, book_no):
        self.book_view.show_book(self.book_model.get_book(book_no))

    def add_book(self, title, price):
        self.book_model.add_book(title, price)

    def update_book(self, book_no, title, price):
        self.book_model.update_book(book_no, title, price)

    def delete_book(self, book_no):
        self.book_model.delete_book(book_no)
