# Library model

class Library:

    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        return True

    def duplicate_book(self, title):
        for existing_book in self.books:
            if existing_book.title == title:
                return True

        return False

    def remove_book(self, title):
        for book in self.books:
            if book.title == title:
                self.books.remove(book)
                return True

        return False

    def view_book_list(self):
        return self.books

    def search_book(self, title):
        for book in self.books:
            if book.title == title:
                return book

        return None

    def update_status(self, title, status):
        for book in self.books:
            if book.title == title:
                book.status = status
                return True

        return False