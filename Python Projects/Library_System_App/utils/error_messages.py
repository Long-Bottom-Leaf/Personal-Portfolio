# Program error messages

INVALID_MENU_CHOICE = (
    "\nError: Invalid menu choice. Please select a valid option.\n"
)

INVALID_STATUS_CHOICE = (
    "\nError: Invalid status. Please enter Y/N for read or unread.\n"
)

# Adding book error messages
ERROR_ADDING_BOOK = (
    "\nError: Unable to add book, please ensure book details are input correctly.\n"
)

DUPLICATE_BOOK = (
    "\nError: Book has already been added. Choose option 4 to update status of the book, or 5 to update any of the book details.\n"
)

# Book update error messages
DUPLICATE_AUTHOR = (
    "\nError: The author provided is already assigned to this book.\n"
)

DUPLICATE_GENRE = (
    "\nError: The genre provided is already assigned to this book.\n"
)

DUPLICATE_RELEASE_DATE = (
    "\nError: The date provided is already assigned to this book.\n"
)

DUPLICATE_RATING = (
    "\nError: The rating provided is already assigned to this book.\n"
)

DUPLICATE_STATUS = (
    "\nError: The status provided is already assigned to this book.\n"
)

ERROR_UPDATING_BOOK = (
    "\nError: Book was not updated correctly, please try again.\n"
)

# Library messages
EMPTY_LIBRARY = (
    "\nError: No books found. Please add a book/s to the library.\n"
)

INVALID_LIBRARY_DATA = (
    "\nError: The library data could not be loaded."
    "The library will start empty.\n"
)

# Book detail error messages
EMPTY_TITLE = (
    "\nError: Book title cannot be empty. Please enter a valid book title.\n"
)

EMPTY_AUTHOR = (
    "\nError: Book author cannot be empty. Please enter a valid book author.\n")

EMPTY_GENRE = (
    "\nError: Book genre cannot be empty. Please enter a valid book genre.\n"
)

EMPTY_STATUS = (
    "\nError: Book status cannot be empty. Please enter a valid book status.\n"
)

RELEASE_DATE_ERROR = (
    "\nError: Invalid date. Please enter a valid book release date or leave empty.\n"
)

INVALID_RATING = (
    "\nError: Invalid rating. Please enter a valid rating 0-5, or leave empty.\n"
)

# Filter options
INVALID_BOOK_TITLE = (
    "\nError: No book was found with that title. Please enter another book title, or add the book to the library.\n"
)

INVALID_AUTHOR = (
    "\nError: No author found. Please search for another author.\n"
)

INVALID_GENRE = (
    "\nError: Could not find books with this genre. Please enter another genre.\n"
)

INVALID_STATUS_SEARCH = (
    "\nError: Could not find any books with this status. Please enter another status (Read/Unread).\n"
)