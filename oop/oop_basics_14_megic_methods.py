#Dunder methods

class Book:
    def __init__(self, title, author, num_pages):
        self.title = title
        self.author = author
        self.num_pages = num_pages

    def __str__(self): 
        return f"{self.title} by {self.author} with {self.num_pages} pages"
    
    def __eq__(self, other):
        return self.num_pages == other.num_pages and self.title == other.title and self.author == other.author
    
    def __gt__(self, other):
        return self.num_pages > other.num_pages
    
    def __add__(self, other):
        return self.num_pages + other.num_pages
    
    def __contains__(self, word):
        return word in self.title
    
    def __getitem__(self, key):
        # return getattr(self, key) #or
        return [self.title if key == 'title' else self.author if key == 'author' else self.num_pages if key == 'num_pages' else f'{key} is not a valid key'][0] #with 0 list is converted to string
    
book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", 180)
book2 = Book("The Catcher in the Rye", "J.D. Salinger", 234)
book3 = Book("The Lord of the Rings", "J.R.R Tolkien", 1178)
book4 = Book("The Lord of the Rings", "J.R.R Tolkien", 1178)
book5 = Book("The Lord of the Rings", "J.R.R Tolkien", 234)

print(book1) #Here only memory will be shown which can be corrected by printing book1.title or with __str__ method
print(book1==book2) #shows False - correct
print(book3==book4) #shows False - incorrect, which can be corrected with a method called __eq__. Now shows True which is correct
print(book5==book4) #shows False - correct, as no of pages are different

# print(book4 < book5) #cannot be used between objects
print(book4.num_pages > book5.num_pages)
#or dunder __gt__ can be used too
print(book4 > book5) #can be used between objects when there is a dunder method
print(book4 + book5)
print('Catcher' in book2) #dunder contains
print(book1['title']) #gives error and hence getitem dunder
print(book1['author'])
print(book1['num_pages'])
print(book1['Hero'])