# Personal Library System

A command-line application built with Python that allows users to manage a personal book collection. Users can add, view, search, filter, update, and remove books, track their reading status, and save their library between sessions using JSON persistence.

## Features

- **Add Books** — Add books with a title, author, genre, release date, rating, and reading status.
- **View Library** — Display all books in the collection.
- **Search Books** — Find individual books by title or search by author.
- **Filter Books** — Filter the collection by genre or reading status.
- **Update Book Details** — Modify existing book information, including its reading status.
- **Remove Books** — Remove books from the collection, with the option to remove multiple books in one session.
- **Track Reading Status** — Mark books as read or unread.
- **Book Statistics** — View the total number of books in the library.
- **Data Persistence** — Save and load the collection using a JSON file, allowing data to persist between application sessions.
- **Input Validation** — Validate user input and handle errors such as duplicate titles, missing books, invalid ratings, and invalid dates.

## Technologies Used

- Python
- JSON
- `unittest`
- `unittest.mock`

## Project Structure

```text
Personal-Library-System/
├── models/
│   ├── book.py
│   └── library.py
├── services/
│   └── persistence.py
├── utils/
│   ├── validators.py
│   ├── error_messages.py
│   ├── success_messages.py
│   └── menus.py
├── tests/
│   ├── test_book.py
│   ├── test_library.py
│   ├── test_persistence.py
│   └── test_validators.py
├── data/
│   └── library.json
└── main.py
```

## Getting Started

### Prerequisites

- Python 3.10 or later
- Git (optional, for cloning the repository)

### Installation

1. Clone the repository:

   ```bash
   git clone YOUR_REPOSITORY_URL
   ```

2. Navigate to the project directory:

   ```bash
   cd Personal-Library-System
   ```

3. Run the application:

   ```bash
   python main.py
   ```

No third-party packages are required.

## Running the Tests

The project uses Python's built-in `unittest` framework.

Run the full test suite from the project root:

```bash
python -m unittest discover -s tests -v
```

The tests cover the book model, library operations, searching and filtering, reading status, JSON persistence, and input validation.

## Data Storage

The application stores book information in `data/library.json` using JSON format.

Each book contains the following fields:

- `title` — Book title
- `author` — Author's name
- `genre` — Book genre
- `release_date` — Publication year or date
- `rating` — User rating
- `status` — Reading status (`Read` or `Unread`)

The library is loaded when the application starts and saved when changes are made.

## Design and Implementation

The project uses a modular structure to separate responsibilities:

- **Models** manage book data and library operations.
- **Services** handle data persistence.
- **Utilities** provide input validation, menu functions, and reusable messages.
- **Main application** manages the command-line interface and user interaction.
- **Tests** verify application behaviour and help prevent regressions.

This structure makes the application easier to maintain, test, and extend.

## What I Practised

Building this project helped me practise:

- Object-oriented programming with classes and objects
- Lists, loops, conditionals, and dictionaries
- Modular code organization and separation of concerns
- Input validation and error handling
- Reading and writing JSON data
- Unit testing with `unittest`
- Mocking file operations during tests
- Designing interactive command-line applications

## Future Improvements

Potential improvements include:

- Additional library statistics, such as average rating and most common genre
- Sorting books by title, author, publication date, or rating
- Improved command-line formatting and navigation
- Additional test coverage and edge-case handling
- A graphical or web-based interface

---

**Status:** In development

**Language:** Python