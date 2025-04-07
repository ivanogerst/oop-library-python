class Book():
    
    def __init__(self, title, author, identifier, status = False):
        
        self.title = title
        
        self.author = author
        
        self.__identifier = identifier
        
        self.status = status
        
        
    #returns the private varibale identifier
    def get_identifier(self):
        
        return self.__identifier
    
    #receives two letters, either "T" for True of "F" for False
    def change_status(self, new_status):
        
        while new_status not in ("T", "F"):
            
            new_status = input(f"For book {self.title }, please enter either the letter 'T' if available or 'F' if not available.\n> ")
            
        if new_status == "T":
            
            new_status = True
            
        else:
            
            new_status = False
            
        self.status = new_status
        
    
    
    def __str__(self):
        
        return f"Book title: {self.title}\tAuthor: {self.author}\tStatus: {'Available' if self.status else 'Unavailable'}"
    


class Ebook(Book):
    
    def __init__(self, title, author, identifier, status, size_mb):
        
        super().__init__(title, author, identifier, status)
        
        self.size_mb = size_mb
        
    def __str__(self):
        
        return f"Book title: {self.title}\tAuthor: {self.author}\tStatus: {'Available' if self.status else 'Unavailable'}\tFile size in megabytes: {self.size_mb}"
    
    
    
class Patron():
    
    def __init__(self, name: str, patron_id: str):
        
        self.name = name
        
        self.__patron_id = patron_id
        
        self.borrowed_books = []
        
    #adds a book to selected patron's profile
    def add_books(self, added_book: Book):
        
        self.borrowed_books.append(added_book)
        
        print(f"\nYou've successfully added '{added_book.title}' from author '{added_book.author}' to your list!")
        
    def remove_books(self, removed_book):
        
        if removed_book not in self.borrowed_books:
            
            print("No borrowed book with that title!")
            
        else:
            
            print(f"You've succesfully removed '{removed_book}' from {self.name}'s cart.")
            
            self.borrowed_books.remove(removed_book)
            
    def __str__(self):
        
        if not self.borrowed_books:
            
            return "Patron has no borrowed books."
        
        borrowed_books_str = "\n".join([book.title for book in self.borrowed_books])
        
        return f"\nPatron's name: {self.name}\nPatron's borrowed books:\n{borrowed_books_str}"
    
    

class Library:
    
    
    def __init__(self, book_collection=None, patron_list=None):
        
        self.book_collection = book_collection if book_collection else []
        
        self.patron_list = patron_list if patron_list else []
        
        for book in self.book_collection:
            
            book.status = True
        
        
    def add_books(self, added_book: Book):
        
        self.book_collection.append(added_book)
        
        added_book.status = True
        
        print(f"\nYou've successfully added '{added_book.title}' from author '{added_book.author}' to the library!")
        
        
    def add_patrons(self, added_patron: Patron):
        
        self.patron_list.append(added_patron)
        
        print(f"\nYou've successfully added '{added_patron.name}' as a Patron!")
        
        
    def checkout_to_patron(self, selected_book: {Book or Ebook}, selected_patron: Patron):
        
        if selected_book.status:
            
            self.book_collection.remove(selected_book)
            
            selected_patron.add_books(selected_book)
            
            if selected_book not in self.book_collection:
                
                selected_book.status = False
            
        else:
            
            print("The book isn't available.")
            
            
    def return_books(self, selected_book: {Book or Ebook}, selected_patron: Patron):
        
        selected_patron.remove_books(selected_book)
        
        self.book_collection.append(selected_book)
        
        selected_book.status = True
        
        print(f"{selected_patron} successfully returned {selected_book.title} to the library!")
        
        
    def display_collection(self):
        
        for i in self.book_collection:
            
            print(f"\n{i}")
            
            
    def display_patrons(self):
        
        for patron in range(len(self.patron_list)):
            
            print(f"\n\n{patron + 1}. {self.patron_list[patron].name}")
            
            for book in self.patron_list[patron].borrowed_books:
                
                print(f"\n{book}")
                
    def search_book(self, book_title = "", book_author = ""):
        
        for book in self.book_collection:
            
            if book.title == book_title or book.author == book_author:
                
                print(book)