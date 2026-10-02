# Library System Main

from models.book import Book
from models.library import Library
from services.persistence import (save_library, load_library)
from utils.validators import (
    validate_menu_choice,
    validate_non_empty,
    validate_rating,
    validate_release_date,
    validate_status,
    BOOK_STATUS,
)
from utils.error_messages import (
    INVALID_MENU_CHOICE,
    INVALID_STATUS_CHOICE,
    ERROR_ADDING_BOOK,
    DUPLICATE_BOOK,
    ERROR_UPDATING_BOOK,
    EMPTY_LIBRARY,
    EMPTY_TITLE,
    EMPTY_AUTHOR,
    EMPTY_GENRE,
    RELEASE_DATE_ERROR,
    EMPTY_RATING,
    INVALID_BOOK_TITLE,
    INVALID_LIBRARY_DATA,
    INVALID_AUTHOR,
    INVALID_GENRE,
    INVALID_STATUS,
)
from utils.success_messages import (
    BOOK_ADDED,
    BOOK_UPDATE,
    BOOK_REMOVED,
)

def display_menu():
    print("\n==== Library Menu ====")

    print("\n1. Add new book")
    print("\n2. View book library")
    print("\n3. View specific book")
    print("\n4. Mark book as read/unread")
    print("\n5. Update book details")
    print("\n6. View total books in library")
    print("\n7. Search/Filter options")
    print("\n8. Remove a book")

    print("\n9. Exit\n")

def book_update_menu():
    print("\n==== Update Book Details ====")

    print("\n1. Title")
    print("\n2. Author")
    print("\n3. Genre")
    print("\n4. Release Date (YYYY-MM-DD)")
    print("\n5. Rating")
    print("\n6. Status")
    print("\n7. Exit")

def search_menu():
    print("\n==== Search Menu====")

    print("\nSearch by: ")
    print("\n1. Author")
    print("\n2. Genre")
    print("\n3. Read/Unread")
    print("\n4. Exit")

def main():
    library, loaded = load_library()

    if not loaded:
        print(INVALID_LIBRARY_DATA)

    while True:
        display_menu()

        choice = input("Enter an option: ")

        if not validate_menu_choice(choice, ["1", "2", "3", "4", "5", "6", "7", "8", "9"]):
            print(INVALID_MENU_CHOICE)
            continue

        match choice:
            case "1":
                print("\n==Enter book details==\n")
                title = input("Enter title: ").strip().title()
                if not validate_non_empty(title):
                    print(EMPTY_TITLE)
                    continue

                if library.duplicate_book(title):
                    print(DUPLICATE_BOOK)
                    continue

                author = input("Enter author: ").strip().title()
                if not validate_non_empty(author):
                    print(EMPTY_AUTHOR)
                    continue

                genre = input("Enter genre: ").strip().title()
                if not validate_non_empty(genre):
                    print(EMPTY_GENRE)
                    continue

                release_date = input("Enter the release date (YYYY-MM-DD) or leave empty: ")
                if not validate_release_date(release_date):
                    print(RELEASE_DATE_ERROR)
                    continue

                rating = input("Enter rating out of 5, if any: ")
                if not validate_rating(rating):
                    print(EMPTY_RATING)
                    continue

                status = input("Have you read this book? (Y/N): ").strip().upper()
                if not validate_non_empty(status) or status not in BOOK_STATUS:
                    print(INVALID_STATUS_CHOICE)
                    continue

                book = Book(
                    title,
                    author,
                    genre,
                    release_date,
                    rating,
                    status
                )

                if library.add_book(book):
                    save_library(library)
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
                title = input("\nEnter the book title you want to view: ").strip().title()
                book = library.search_book(title)

                if book is None:
                    print(INVALID_BOOK_TITLE)

                else:
                    print(book)

            case "4":
                title = input("Enter the title of the book you wish to change the status of: ").strip().title()
                status = input("Enter Y or N for read/unread: ").strip().upper()
                

                if status not in BOOK_STATUS:
                    print(INVALID_STATUS_CHOICE)

                else:
                    if library.update_status(title, BOOK_STATUS[status]):
                        save_library(library)
                        print(BOOK_UPDATE)

                    else:
                        print(ERROR_UPDATING_BOOK)

            case "5":
                title = input("Enter the title of the book you want to update: ").strip().title()
                book = library.search_book(title)

                if book is None:
                    print(INVALID_BOOK_TITLE)

                else:
                    while True:
                        book_update_menu()
                        
                        choice = input("Enter an option: ")
                                            
                        if not validate_menu_choice(choice, ["1", "2", "3", "4", "5", "6", "7"]):
                            print(INVALID_MENU_CHOICE)
                            continue

                        match choice:
                            case "1":
                                new_title = input("Enter the new title: ").strip().title()

                                if not validate_non_empty(new_title):
                                    print(EMPTY_TITLE)
                                    continue

                                if new_title != book.title and library.duplicate_book(new_title):
                                    print(DUPLICATE_BOOK)
                                    continue

                                book.title = new_title
                                save_library(library)
                                print(BOOK_UPDATE)

                            case "2":
                                new_author = input("Enter the new author: ").strip().title()

                                if not validate_non_empty(new_author):
                                    print(EMPTY_AUTHOR)
                                    continue

                                if new_author != book.author:
                                    print() # error message
                                    continue

                                book.author = new_author
                                save_library(library)
                                print(BOOK_UPDATE)

                            case "3":
                                new_genre = input("Enter the new genre: ").strip().title()

                                if not validate_non_empty(new_genre):
                                    print(EMPTY_GENRE)
                                    continue

                                if new_genre != book.genre:
                                    print() # error message
                                    continue

                                book.genre = new_genre
                                save_library(library)
                                print(BOOK_UPDATE)

                            case "4":
                                new_release_date = input("Enter the new release date (YYYY-MM-DD): ")

                                if not validate_release_date(new_release_date):
                                    print() # error message
                                    continue

                                if new_release_date != book.release_date:
                                    print() # error message
                                    continue

                                book.release_date = new_release_date
                                save_library(library)
                                print(BOOK_UPDATE)

                            case "5":
                                new_rating = input("Enter a new rating (0-5): ").strip()

                                if not validate_rating(new_rating):
                                    print() # error message
                                    continue

                                if new_rating != book.rating:
                                    print() # error message
                                    continue

                                book.rating = new_rating
                                save_library(library)
                                continue

                            case "6":
                                new_status = input("Enter a new status for read/unread (Y/N): ") # fix later

                                if not validate_status(new_status):
                                    print() # error message
                                    continue

                                book.status = new_status
                                save_library(library)
                                continue

                            case "7":
                                save_library(library)
                                print("Returning to main menu!")
                                break

            case "6":
                book_total = library.total_books()
                
                if not library.books:
                    print(EMPTY_LIBRARY)
                
                else:
                    print(book_total)

            case "7":
                while True:
                    search_menu()

                    choice = input("Enter an option: ")
                    
                    if not validate_menu_choice(choice, ["1", "2", "3", "4"]):
                        print(INVALID_MENU_CHOICE)
                        continue

                    match choice:
                        case "1":
                            author = input("Enter the authors name: ").strip().title()

                            if not author:
                                print(INVALID_AUTHOR)

                            else:
                                books = library.search_by_author(author)
                                if not books:
                                    print(INVALID_AUTHOR)

                                else:
                                    for book in books:
                                        print(book)

                        case "2":
                            genre = input("Enter the genre: ").strip().title()

                            if not genre:
                                print(INVALID_GENRE)

                            else:
                                books = library.search_by_genre(genre)
                                if not books:
                                    print(INVALID_GENRE)

                                else:
                                    for book in books:
                                        print(book)

                        case "3":
                            status = input("Enter a status (Read/Unread): ").strip().title()

                            if not status:
                                print(INVALID_STATUS)

                            else:
                                books = library.search_by_status(status)
                                if not books:
                                    print(INVALID_STATUS)

                                else:
                                    for book in books:
                                        print(book)

                        case "4":
                            save_library(library)
                            print("Returning to main menu!")
                            break

            case "8":
                title = input("Enter the book title to be removed: ").strip().title()
            
                if library.remove_book(title):
                    save_library(library)
                    print(BOOK_REMOVED)
                                
                else:
                    print(INVALID_BOOK_TITLE)

            case "9":
                save_library(library)
                print("Goodbye")
                break

if __name__ == "__main__":
    main()