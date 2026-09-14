# Library Persistence Service

import json
import os

from models.book import Book
from models.library import Library


DATA_FILE = os.path.join(
    os.path.dirname(os.path.dirname(__file__)),
    "data",
    "library.json"
)


def save_library(library):
    books_data = []

    for book in library.books:
        book_data = {
            "title": book.title,
            "author": book.author,
            "genre": book.genre,
            "release_date": book.release_date,
            "rating": book.rating,
            "status": book.status
        }

        books_data.append(book_data)

    with open(DATA_FILE, "w") as file:
        json.dump(books_data, file, indent=4)


library = Library()

book = Book(
    "Cool Book",
    "John French",
    "Horror",
    1999,
    5,
    "Unread"
)

library.add_book(book)

save_library(library)