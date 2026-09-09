# Library System Main

from models.book import Book
from models.library import Library
from utils.validators import (
    validate_menu_choice,
    BOOK_STATUS,
)
from utils.error_messages import (
    INVALID_MENU_CHOICE,
    INVALID_STATUS_CHOICE,
    ERROR_UPDATING_BOOK,
    INVALID_BOOK_TITLE
)
from utils.success_messages import (
    BOOK_ADDED,
    BOOK_UPDATE,
    EMPTY_LIBRARY,
    ERROR_ADDING_BOOK,
)

def display_menu():
    print("\n==== Library Menu ====")

    print("\n1. Add new book")
    print("\n2. View book library")
    print("\n3. View specific book")
    print("\n4. Mark book as read/unread")
    print("\n5. Update book details")
    print("\n6. Remove a book")

    print("\n6. Exit")

def main():

    library = Library()

    while True:
        display_menu()

        choice = input("Enter an option: ")

        if not validate_menu_choice(choice, ["1", "2", "3", "4", "5", "6", "7"]):
            print(INVALID_MENU_CHOICE)
            continue

        match choice:
            case "1":
                print("\n==Enter book details==\n")
                title = input("Enter title: ").strip().upper()
                author = input("Enter author: ").strip().upper()
                genre = input("Enter genre: ").strip().upper()
                release_date = input("Enter the release date: ")
                rating = input("Enter rating, if any: ")
                status = input("Have you read this book? (Y/N): ").strip().upper()

                book = Book(
                    title,
                    author,
                    genre,
                    release_date,
                    rating,
                    status
                )

                if library.add_book(book):
                    print(BOOK_ADDED)

                else:
                    print(ERROR_ADDING_BOOK)

            case "2":
                print("\n==Library List==\n")

                books = library.view_book_list()

                if not books:
                    print(EMPTY_LIBRARY)

                else:
                    for book in books:
                        print(book)

            case "3":
                title = input("\nEnter the book title you want to view: ").strip().upper()
                book = library.search_book(title)

                if book is None:
                    print(INVALID_BOOK_TITLE)

                else:
                    print(book)

            case "4":
                title = input("Enter the title of the book you wish to change the status of: ").strip().upper()
                status = input("Enter Y or N for read/unread: ").strip().upper()

                if status not in BOOK_STATUS:
                    print(INVALID_STATUS_CHOICE)

                else:
                    if library.update_status(title, BOOK_STATUS[status]):
                        print(BOOK_UPDATE)

                    else:
                        print(ERROR_UPDATING_BOOK)

            case "5":
                title = input("Enter the title of the book you want to update: ").strip().upper()
                book = library.search_book(title)

                if not books:
                    print(EMPTY_LIBRARY)
                
                else:
                    for book in books:
                        print(book)

                    # will finish after tests

            case "6":
                title = input("Enter the book title to be removed: ").strip().upper()
            
                if library.remove_book(title):
                    print("Book removed successfully!")
                                
                else:
                    print(INVALID_BOOK_TITLE)

            case "7":
                print("Goodbye")
                break

if __name__ == "__main__":
    main()