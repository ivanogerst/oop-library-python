class Book():
    
    def __init__(self, title, author, unique_number, status):
        
        self.title = title
        
        self.author = author
        
        self.__unique_number = unique_number
        
        self.status = status
        
        
    #returns the private varibale unique_number
    def get_number(self):
        
        return self.__unique_number
    
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
    
    