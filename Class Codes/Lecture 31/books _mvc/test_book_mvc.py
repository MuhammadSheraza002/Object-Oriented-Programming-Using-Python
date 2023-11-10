from book_controller import *
from book_model import *
from book_view import *

bc = Book_Controller(Book_Model(), Book_View())
bc.add_book('How to pass without study',5000000000000000)
bc.add_book('How to get job without apply',6000000000000000)
bc.add_book('How to continue job without work',8000000000000000)
bc.show_books()
bc.show_book(2)
bc.update_book(2, 'How to get money without effort', 9000000000000000)
bc.show_book(2)
bc.add_book('Cash Book', 1000)
bc.show_books()
bc.delete_book(4)
bc.show_books()
