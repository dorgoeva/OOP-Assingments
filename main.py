class Book:
    def __init__(self):
        self.title = None
        self.author = None
        self.ISBN = None
        self.price = None

    def set_details(self, title, author, ISBN, price):
        self.title = title
        self.author = author
        self.ISBN = ISBN
        self.price = price
