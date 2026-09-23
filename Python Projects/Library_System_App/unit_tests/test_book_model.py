# Book

import sys
import os
import unittest

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from models.book import Book

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