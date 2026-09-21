# Persistence service tests

import json
import sys
import os
import unittest

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from models.book import Book
from models.library import Library
from services.persistence import save_library, load_library, DATA_FILE

from unittest.mock import mock_open, patch

class TestPersistence(unittest.TestCase):

    @patch("services.persistence.json.dump")
    @patch("services.persistence.open", new_callable = mock_open)
    def test_save_library(self, mock_file, mock_json_dump):
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
        save_library(library)

        mock_file.assert_called_once_with(DATA_FILE, "w")

        mock_json_dump.assert_called_once_with(
            [
                {
                    "title": "Cool Book",
                    "author": "John French",
                    "genre": "Horror",
                    "release_date": 1999,
                    "rating": 5,
                    "status": "Unread"
                }
            ],
            mock_file(),
            indent=4
        )

    def test_save_library_empty(self):
        library = Library()
        save_library(library)

        with open(DATA_FILE, "r") as file:
            data = file.read()

        self.assertEqual(data, "[]")

    @patch("services.persistence.json.dump")
    @patch("services.persistence.open", new_callable=mock_open)
    def test_save_library_multiple_books(self, mock_file, mock_json_dump):
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
            "Super Cool Book",
            "Adam Adams",
            "Comedy",
            2001,
            6,
            "Read"
        )

        library.add_book(book1)
        library.add_book(book2)
        save_library(library)

        with open(DATA_FILE, "r") as file:
            data = file.read()

        mock_file.assert_called_once_with(DATA_FILE, "w")

        mock_json_dump.assert_called_once_with(
            [
                {
                    "title": "Cool Book",
                    "author": "John French",
                    "genre": "Horror",
                    "release_date": 1999,
                    "rating": 5,
                    "status": "Unread"
                },
                {
                    "title": "Super Cool Book",
                    "author": "Adam Adams",
                    "genre": "Comedy",
                    "release_date": 2001,
                    "rating": 6,
                    "status": "Read"
                }
            ],
            mock_file(),
            indent=4
        )

    @patch("services.persistence.json.load")
    @patch("services.persistence.open", new_callable=mock_open)
    def test_load_library(self, mock_file, mock_json_load):
        mock_json_load.return_value = [
            {
                "title": "Cool Book",
                "author": "John French",
                "genre": "Horror",
                "release_date": 1999,
                "rating": 5,
                "status": "Unread"
            }
        ]
    
        library = load_library()
    
        book = library.books[0]
    
        self.assertEqual(book.title, "Cool Book")
        self.assertEqual(book.author, "John French")
        self.assertEqual(book.genre, "Horror")
        self.assertEqual(book.release_date, 1999)
        self.assertEqual(book.rating, 5)
        self.assertEqual(book.status, "Unread")

    @patch("services.persistence.os.path.exists")
    def test_load_library_missing_file(self, mock_exists):
        mock_exists.return_value = False

        library = load_library()

        self.assertIsInstance(library, Library)
        self.assertEqual(library.books, [])

    @patch("services.persistence.os.path.exists")
    def test_load_library_missing_file(self, mock_exists):
        mock_exists.return_value = False

        library = load_library()

        self.assertIsInstance(library, Library)
        self.assertEqual(library.books, [])

    @patch("services.persistence.json.load")
    @patch("services.persistence.open", new_callable=mock_open)
    def test_load_library_multiple_books(self, mock_file, mock_json_load):
        mock_json_load.return_value = [
            {
                "title": "Cool Book",
                "author": "John French",
                "genre": "Horror",
                "release_date": 1999,
                "rating": 5,
                "status": "Unread"
            },
            {
                "title": "Really Cool Book",
                "author": "John Harris",
                "genre": "Drama",
                "release_date": 2005,
                "rating": 6,
                "status": "Read"
            }
        ]

        library = load_library()

        self.assertEqual(len(library.books), 2)

        self.assertEqual(library.books[0].title, "Cool Book")
        self.assertEqual(library.books[0].author, "John French")

        self.assertEqual(library.books[1].title, "Really Cool Book")
        self.assertEqual(library.books[1].author, "John Harris")

    @patch("services.persistence.json.load")
    @patch("services.persistence.open", new_callable=mock_open)
    def test_load_library_invalid_json(self, mock_file, mock_json_load):
        mock_json_load.side_effect = json.JSONDecodeError(
            "Invalid JSON",
            "",
            0
        )

        library = load_library()

        self.assertIsInstance(library, Library)
        self.assertEqual(library.books, [])

if __name__ == '__main__':
    unittest.main()