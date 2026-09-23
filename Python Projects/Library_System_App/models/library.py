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

    def update_status(self, title, status):
        for book in self.books:
            if book.title == title:
                book.status = status
                return True

        return False

    def search_book(self, title):
        for book in self.books:
            if book.title == title:
                return book

        return None

    def search_by_author(self, author):
        matching_books = []

        for book in self.books:
            if book.author == author:
                matching_books.append(book)

        return matching_books

    def search_by_genre(self, genre):
        matching_books = []

        for book in self.books:
            if book.genre == genre:
                matching_books.append(book)

        return matching_books

    def search_by_status(self, status):
        matching_books = []

        for book in self.books:
            if book.status == status:
                matching_books.append(book)

        return matching_books

    def total_books(self):
        return len(self.books)

    def books_read(self):
        count = 0

        for book in self.books:
            if book.status == "Y":
                count += 1

        return count