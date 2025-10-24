# Practice object-oriented programming, attributes, and methods. Build a basic system to 
# manage books in a library.

# 🧠 Requirements:

# Create a Book class with:
# Attributes: title, author, year, is_checked_out (default = False)
# Method: checkout() → sets is_checked_out = True
# Method: return_book() → sets is_checked_out = False
# Method: str() → returns a string like: "1984 by George Orwell (Checked out: False)"

class Book:
    def __init__(self, title, author, year, is_checked_out = False):
        self.title = title
        self.author = author
        self.year = year
        self.is_checked_out = is_checked_out

    def checkout(self):
        if not self.is_checked_out:
            self.is_checked_out = True
        else:
            print("already checked out")
    
    def return_book(self):
        if self.is_checked_out:
            self.is_checked_out = False
        else:
            print("was not checked out")
    
    def string(self):
        return f'{self.title} by {self.author} (Checked out: {self.is_checked_out})'

# Create a Library class with:
# Attribute: a list called collection to store books
# Method: add_book(book) → adds to collection
# Method: list_books() → prints all book titles and status
# Method: find_book(title) → returns a matching book (case-insensitive)

class Library:
    def __init__(self):
        self.collection = []
    
    def add_book(self, book):
        self.collection.append(book)
        print(f'{book.title} added to te Library')

    def list_books(self):
        if not self.collection:
            print("Library is empty")
        
        else:
            for book in self.collection:
                print("-", book.title, book.is_checked_out)

    def find_book(self, title):
        for book in self.collection:
            if book.title.lower() == title.lower():
                return f'{book.title} is found'
        
        print("Not found")
        return None

b1 = Book('1984', 'George Orwell', 1949)
b2 = Book('The Alchemist', 'Paulo Coelho', 1988)

lib = Library()
lib.add_book(b1)
lib.add_book(b2)

lib.list_books()

b1.checkout()
lib.list_books()

found = lib.find_book('1984')
print(found)