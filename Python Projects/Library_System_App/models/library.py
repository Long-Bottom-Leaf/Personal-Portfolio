# Library model

class Library:

    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, title):
        for book in self.books:
            if book.title == title:
                self.books.remove(book)
                return

    def view_book_list(self):
        for book in self.books:
            print(book)

    def view_specific_book(self, title):
        for book in self.books:
            if book.title == title:
                print(book)
                return book
