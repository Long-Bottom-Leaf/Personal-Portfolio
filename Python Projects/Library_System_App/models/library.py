# Library model

class Library:

    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        return True

    def remove_book(self, title):
        for book in self.books:
            if book.title == title:
                self.books.remove(book)
                return True

        return False

    def view_book_list(self):
        for book in self.books:
            print(book)

    def search_book(self, title):
        for book in self.books:
            if book.title == title:
                print(book)
                return book

    def update_status(self, title, status):
        for book in self.books:
            if book.title == title:
                book.status = status
                return True

        return False