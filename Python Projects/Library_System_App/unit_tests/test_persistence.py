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

if __name__ == '__main__':
    unittest.main()