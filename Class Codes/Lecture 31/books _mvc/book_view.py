from book import *
class Book_View:
    def show_book(self, book):
        print('--- BOOK DETAILS ---')
        print(book)

    def show_books(self, books):
        print('--- Books ---')
        for i, book in enumerate(books):
            print(f'{i+1}. {book}')
