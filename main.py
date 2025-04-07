from classes import Book, Ebook, Patron, Library

def main():
    book1 = Book("The Hidden Grove", "Lana Rivers", "ID001", True)
    book2 = Book("Echoes in the Fog", "Miles Kendrick", "ID002", True)
    ebook1 = Ebook("Virtual Horizons", "Nia Monroe", "E001", True, 5.4)

    patron1 = Patron("Alice", "P001")
    patron2 = Patron("Bob", "P002") 

    library = Library()
    library.add_books(book1)
    library.add_books(book2)
    library.add_books(ebook1)
    library.add_patrons(patron1)
    library.add_patrons(patron2)
    
    print("\nCurrent Library Collection:")
    library.display_collection()

    
    print("\nChecking out a book to Alice...")
    library.checkout_to_patron(book1, patron1)

    print("\nLibrary Collection After Checkout:")
    library.display_collection()

    print("\nPatron Info:")
    library.display_patrons()

    print("\nSearching for books by author 'Miles Kendrick':")
    library.search_book(book_author="Miles Kendrick")

    print("\nReturning book to library...")
    library.return_books(book1, patron1)

    print("\nLibrary Collection After Return:")
    library.display_collection()


if __name__ == "__main__":
    main()
