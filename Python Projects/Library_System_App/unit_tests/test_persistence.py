import sys
import os
import unittest

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from models.book import Book
from models.library import Library
from services.persistence import save_library, DATA_FILE

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

if __name__ == '__main__':
    unittest.main()