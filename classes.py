class Book():
    
    def __init__(self, title, author, identifier, status):
        
        self.title = title
        
        self.author = author
        
        self.__identifier = identifier
        
        self.status = status
        
        
    #returns the private varibale identifier
    def get_identifier(self):
        
        return self.__identifier
    
    #receives two letters, either "T" for True of "F" for False
    def change_status(self, new_status):
        
        while new_status != "T" or "F":
            
            new_status = input(f"For book {self.title }, please enter either the letter 'T' if available or 'F' if not available.\n> ")
            
        if new_status == "T":
            
            new_status = True
            
        else:
            
            new_status = False
            
        self.status = new_status
        
    
    
    def __str__(self):
        
        return f"Book title: {self.title}\tAuthor: {self.author}\tStatus: {'Available' if self.status else 'Unavailable'}"
    
    
    
class Patron():
    
    def __init__(self, name: str, patron_id: str):
        
        self.name = name
        
        self.__patron_id = patron_id
        
        self.borrowed_books = []
        
    def add_books(self, added_book: Book):
        
        self.borrowed_books.append(added_book)
        
        print(f"Uspješno ste dodali knjigu '{added_book.title}' autora '{added_book.author}'!")
        
    def remove_books(self):
        
        if len(self.borrowed_books) == 0:
            
            print("There are no books that you've borrowed!")
            
        else:
            
            print("Your books:")
            
            for i in range(len(self.borrowed_books)):
                
                print(f"\n{i + 1}. {self.borrowed_books[i]}\n")
            
            removed_book = int(input("\nPlease enter number of the book that you want to remove: "))
            
            print(f"You've succesfully removed '{self.borrowed_books[removed_book - 1].title}' from your cart,")
            
            self.borrowed_books.pop(removed_book - 1)
            
    def __str__(self):
        
        return f"Patron's name: {self.name}\nPatron's borrowed books:\n".join([book.title for book in self.borrowed_books])