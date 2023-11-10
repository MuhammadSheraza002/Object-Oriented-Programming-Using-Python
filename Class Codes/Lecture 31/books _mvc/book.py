class Book:
    book_count = 0
    def __init__(self, title, price):
        Book.book_count += 1
        self.__book_no = Book.book_count
        self.__title = title
        self.__price = price
    def get_book_no(self):
        return self.__book_no
    def get_title(self):
        return self.__title
    def get_price(self):
        return self.__price
    def set_title(self, title):
        self.__title = title
    def set_price(self, price):
        self.__price = price
    def __str__(self):
        return f'Book No: {self.__book_no}\tTitle:{self.__title:<35}\tPrice: {self.__price}'
