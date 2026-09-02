# Book and Library tests

import sys
import os
import unittest

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from models.book import Book
from models.library import Library

class TestBook(unittest.TestCase):

    def test_book_model(self):
        book = Book(
            "Cool Book",
            "John French",
            "Horror",
            1999,
            5,
            "Unread"
        )

        self.assertEqual(book.title, "Cool Book")
        self.assertEqual(book.author, "John French")
        self.assertEqual(book.genre, "Horror")
        self.assertEqual(book.release_date, 1999)
        self.assertEqual(book.rating, 5)
        self.assertEqual(book.status, "Unread")

    def test_book_string(self):
        book = Book(
            "Cool Book",
            "John French",
            "Horror",
            1999,
            5,
            "Unread"
        )

        expected = (
            "Title: Cool Book\n"
            "Author: John French\n"
            "Genre: Horror\n"
            "Release Date: 1999\n"
            "Rating: 5\n"
            "Status: Unread\n"
        )

        self.assertEqual(str(book), expected)

class TestLibrary(unittest.TestCase):

    def test_library_starts_empty(self):
        library = Library()

        self.assertEqual(len(library.books), 0)

    def test_add_book(self):
        library = Library()

        book1 = Book(
            "Cool Book",
            "John French",
            "Horror",
            1999,
            5,
            "Unread"
        )

        book2 = Book(
            "Really Cool Book",
            "John Harris",
            "Drama",
            2005,
            6,
            "Read"
        )

        library.add_book(book1)
        library.add_book(book2)

        self.assertEqual(len(library.books), 2)
        self.assertEqual(book1, library.books)
        self.assertEqual(book2, library.books)

    def test_remove_book(self):
        library = Library()

        book1 = Book(
            "Cool Book",
            "John French",
            "Horror",
            1999,
            5,
            "Unread"
        )

        library.add_book(book1)
        library.remove_book(book1)

        self.assertEqual(len(library.books), 0)
        self.assertNotIn(book1, library.books)

if __name__ == '__main__':
    unittest.main()