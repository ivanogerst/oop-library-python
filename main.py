from classes import *

book1 = Book("A Game of Thrones", "George R.R. Martin", 0000, True)

book2 = Book("ASOIAF", "George R.R. Martin", 0000, True)

patron1 = Patron("Steve", "aaaa")

print(patron1.borrowed_books)

patron1.add_books(book1)

patron1.add_books(book2)

patron1.borrowed_books

print(patron1)