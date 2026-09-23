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
        self.assertEqual(library.books[0], book1)
        self.assertEqual(library.books[1], book2)

    def test_duplicate_book(self):
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

        self.assertTrue(library.duplicate_book("Cool Book"))

    def test_book_is_not_duplicate(self):
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
            4,
            "Read"
        )

        library.add_book(book1)

        self.assertFalse(library.duplicate_book(book2.title))

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
        library.remove_book("Cool Book")

        self.assertTrue(book1 not in library.books)
        self.assertEqual(len(library.books), 1)
        self.assertEqual(library.books[0], book2)

    def test_remove_nonexistent_book(self):
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
        result = library.remove_book("Uncool Book")

        self.assertFalse(result)
        self.assertEqual(len(library.books), 1)
        self.assertEqual(library.books[0], book1)

    def test_view_library_list(self):
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
        books = library.view_book_list()

        self.assertEqual(books, [book1, book2])

    def test_search_specific_book(self):
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

        search1 = library.search_book("Cool Book")
        search2 = library.search_book("Really Cool Book")
        search3 = library.search_book("Uncool Book")

        self.assertEqual(search1, book1)
        self.assertEqual(search2, book2)
        self.assertIsNone(search3)

    def test_update_book_status(self):
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
        result = library.update_status("Cool Book", "Read")

        self.assertTrue(result)
        self.assertEqual(book1.status, "Read")

    def test_update_book_status_not_found(self):
        library = Library()

        result = library.update_status("Uncool Book", "Read")

        self.assertFalse(result)

if __name__ == '__main__':
    unittest.main()