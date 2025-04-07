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
        
        if new_status != "T" or "F":
            
        
        self.status = new_status
    
    def __str__(self):
        
        return f"Book title: {self.title}\tAuthor: {self.author}\tStatus: {self.status}"
    
    