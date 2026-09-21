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

def load_library():
    library = Library()

    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, "r") as file:
                books_data = json.load(file)

        except json.JSONDecodeError:
            return library

        for book_data in books_data:
            book = Book(
                book_data["title"],
                book_data["author"],
                book_data["genre"],
                book_data["release_date"],
                book_data["rating"],
                book_data["status"]
            )
            library.add_book(book)

    return library