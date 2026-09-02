# Library model

class Library:

    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, book):
        self.books.remove(book)

    def view_book(self, book):
        for book in self.books:
            print(book)