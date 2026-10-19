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
from utils.input_helper import (is_return_previous)
from utils.error_messages import (
    INVALID_MENU_CHOICE,
    INVALID_STATUS_CHOICE,
    ERROR_ADDING_BOOK,
    DUPLICATE_BOOK,
    DUPLICATE_AUTHOR,
    DUPLICATE_GENRE,
    DUPLICATE_RELEASE_DATE,
    DUPLICATE_RATING,
    DUPLICATE_STATUS,
    ERROR_UPDATING_BOOK,
    EMPTY_LIBRARY,
    EMPTY_TITLE,
    EMPTY_AUTHOR,
    EMPTY_GENRE,
    EMPTY_STATUS,
    RELEASE_DATE_ERROR,
    INVALID_RATING,
    INVALID_BOOK_TITLE,
    INVALID_LIBRARY_DATA,
    INVALID_AUTHOR,
    INVALID_GENRE,
    INVALID_STATUS_SEARCH,
)
from utils.success_messages import (
    BOOK_ADDED,
    BOOK_UPDATE,
    BOOK_REMOVED,
    RETURN_TO_MAIN
)
from utils.menus import (
    display_menu,
    book_update_menu,
    search_menu,
)

def main():
    library, loaded = load_library()

    if not loaded:
        print(INVALID_LIBRARY_DATA)

    while True:
        display_menu() # main menu

        choice = input("Enter an option: ").strip()

        if not validate_menu_choice(choice, ["1", "2", "3", "4", "5", "6", "7", "8", "9"]):
            print(INVALID_MENU_CHOICE)
            continue

        match choice:
            case "1": # add book
                return_previous = False

                print("\n==Enter book details==\n")
                while True:
                    title = input("Enter title: ").strip().title()
                    if is_return_previous(title):
                        return_previous = True
                        break

                    if not validate_non_empty(title):
                        print(EMPTY_TITLE)

                    elif library.duplicate_book(title):
                        print(DUPLICATE_BOOK)

                    else:
                        break

                # book details
                while True:
                    author = input("Enter author: ").strip().title()
                    if is_return_previous(author):
                        return_previous = True
                        break

                    if is_return_previous(author):
                        return_previous = True
                        break

                    if validate_non_empty(author):
                        break

                    print(EMPTY_AUTHOR)

                while True:
                    genre = input("Enter genre: ").strip().title()
                    if is_return_previous(genre):
                        return_previous = True
                        break

                    if validate_non_empty(genre):
                        break

                    print(EMPTY_GENRE)

                while True:
                    release_date = input("Enter the release date (YYYY-MM-DD) or leave empty: ").strip()
                    if is_return_previous(release_date):
                        return_previous = True
                        break

                    if validate_release_date(release_date):
                        break

                    print(RELEASE_DATE_ERROR)

                while True:
                    rating = input("Enter rating out of 5, if any: ").strip()
                    if is_return_previous(rating):
                        return_previous = True
                        break

                    if validate_rating(rating):
                        break

                    print(INVALID_RATING)

                while True:
                    status = input("Have you read this book? (Y/N): ").strip().upper()
                    if is_return_previous(status):
                        return_previous = True
                        break

                    if validate_status(status):
                        break

                    print(INVALID_STATUS_CHOICE)

                status = BOOK_STATUS[status]

                book = Book(
                    title,
                    author,
                    genre,
                    release_date,
                    rating,
                    status
                )

                # add book and save library
                if library.add_book(book):
                    save_library(library)
                    print(BOOK_ADDED)

                else:
                    print(ERROR_ADDING_BOOK)
                    continue

            case "2": # view all books
                print("\n==Library List==\n")
                books = library.view_book_list()

                if not books:
                    print(EMPTY_LIBRARY)
                    continue

                else:
                    for book in books:
                        print(book)

            case "3": # search for specific book
                return_previous = False

                while True:
                    title = input("\nEnter the book title you want to view: ").strip().title()
                    if is_return_previous(title):
                        return_previous = True
                        break

                    book = library.search_book(title)
                    if book is None:
                        print(INVALID_BOOK_TITLE)
                        continue
                    
                    else:
                        print()
                        print(book)
                        break

            case "4": # update read/unread status
                return_previous = False

                while True:
                    title = input("Enter the title of the book you wish to change the status of: ").strip().title()
                    if is_return_previous(title):
                        return_previous = True
                        break

                    book = library.search_book(title)
                    
                    if book is None:
                        print(INVALID_BOOK_TITLE)
                        continue
                    
                    while True:
                        status = input("Enter Y or N for read/unread: ").strip().upper()
                        if is_return_previous(status):
                            return_previous = True
                            break

                        if status not in BOOK_STATUS:
                            print(INVALID_STATUS_CHOICE)
                            continue
                        
                        if library.update_status(title, BOOK_STATUS[status]):
                            save_library(library)
                            print(BOOK_UPDATE)
                            break

                        print(ERROR_UPDATING_BOOK)

                    break

            case "5": # update book all details
                return_previous = False

                while True:
                    title = input("Enter the title of the book you want to update: ").strip().title()
                    if is_return_previous(title):
                        return_previous = True
                        break

                    book = library.search_book(title)
                    
                    if book is None:
                        print(INVALID_BOOK_TITLE)
                        continue

                    while True:
                        book_update_menu()

                        choice = input("Enter an option: ").strip()
                        if is_return_previous(choice):
                            return_previous = True
                            break

                        if not validate_menu_choice(choice, ["1", "2", "3", "4", "5", "6", "7"]):
                            print(INVALID_MENU_CHOICE)
                            continue

                        match choice:
                            case "1":
                                return_previous = False

                                new_title = input("Enter the new title: ").strip().title()
                                if is_return_previous(new_title):
                                    return_previous = True
                                    break

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
                                return_previous = False

                                new_author = input("Enter the new author: ").strip().title()
                                if is_return_previous(new_author):
                                    return_previous = True
                                    break

                                if not validate_non_empty(new_author):
                                    print(EMPTY_AUTHOR)
                                    continue

                                if new_author == book.author:
                                    print(DUPLICATE_AUTHOR)
                                    continue

                                book.author = new_author
                                save_library(library)
                                print(BOOK_UPDATE)

                            case "3":
                                return_previous = False

                                new_genre = input("Enter the new genre: ").strip().title()
                                if is_return_previous(new_genre):
                                    return_previous = True
                                    break

                                if not validate_non_empty(new_genre):
                                    print(EMPTY_GENRE)
                                    continue

                                if new_genre == book.genre:
                                    print(DUPLICATE_GENRE)
                                    continue

                                book.genre = new_genre
                                save_library(library)
                                print(BOOK_UPDATE)

                            case "4":
                                return_previous = False

                                new_release_date = input(
                                    "Enter the new release date (YYYY-MM-DD) or leave empty to clear the existing date: "
                                ).strip()
                                if is_return_previous(new_release_date):
                                    return_previous = True
                                    break

                                if not validate_release_date(new_release_date):
                                    print(RELEASE_DATE_ERROR)
                                    continue

                                if new_release_date == book.release_date:
                                    print(DUPLICATE_RELEASE_DATE)
                                    continue

                                book.release_date = new_release_date
                                save_library(library)
                                print(BOOK_UPDATE)

                            case "5":
                                return_previous = False

                                new_rating = input("Enter a new rating (0-5): ").strip()
                                if is_return_previous(new_rating):
                                    return_previous = True
                                    break

                                if not validate_rating(new_rating):
                                    print(INVALID_RATING)
                                    continue

                                if new_rating == str(book.rating).strip():
                                    print(DUPLICATE_RATING)
                                    continue

                                book.rating = new_rating
                                save_library(library)
                                print(BOOK_UPDATE)

                            case "6":
                                return_previous = False

                                new_status = input("Enter a new status for read/unread (Y/N): ").strip().upper()
                                if is_return_previous(new_status):
                                    return_previous = True
                                    break

                                if not validate_status(new_status):
                                    print(INVALID_STATUS_CHOICE)
                                    continue

                                new_status = BOOK_STATUS[new_status]

                                if new_status == book.status:
                                    print(DUPLICATE_STATUS)
                                    continue

                                book.status = new_status
                                save_library(library)
                                print(BOOK_UPDATE)

                            case "7":
                                save_library(library)
                                print(RETURN_TO_MAIN)
                                break

                    break

            case "6": # view total books
                book_total = library.total_books()
                
                if not library.books:
                    print(EMPTY_LIBRARY)
                
                else:
                    print()
                    print(f"Total number of books in library = {book_total}")

            case "7": # search options
                return_previous = False

                while True:
                    search_menu()

                    choice = input("Enter an option: ").strip()
                    if is_return_previous(choice):
                        return_previous = True
                        break
                    
                    if not validate_menu_choice(choice, ["1", "2", "3", "4"]):
                        print(INVALID_MENU_CHOICE)
                        continue

                    match choice:
                        case "1":
                            return_previous = False

                            while True:
                                author = input("Enter the authors name: ").strip().title()
                                if is_return_previous(author):
                                    return_previous = True
                                    break

                                if not author:
                                    print(EMPTY_AUTHOR)
                                    continue

                                books = library.search_by_author(author)
                                if not books:
                                    print(INVALID_AUTHOR)
                                    continue

                                for book in books:
                                    print()
                                    print(book)

                                break

                        case "2":
                            return_previous = False

                            while True:
                                genre = input("Enter the genre: ").strip().title()
                                if is_return_previous(genre):
                                    return_previous = True
                                    break

                                if not genre:
                                    print(EMPTY_GENRE)
                                    continue

                                books = library.search_by_genre(genre)
                                if not books:
                                    print(INVALID_GENRE)
                                    continue

                                for book in books:
                                    print()
                                    print(book)

                                break

                        case "3":
                            return_previous = False

                            while True:
                                status = input("Enter a status (Read/Unread): ").strip().title()
                                if is_return_previous(status):
                                    return_previous = True
                                    break

                                if not status:
                                    print(EMPTY_STATUS)
                                    continue

                                books = library.search_by_status(status)
                                if not books:
                                    print(INVALID_STATUS_SEARCH)
                                    continue

                                for book in books:
                                    print()
                                    print(book)

                                break

                        case "4":
                            save_library(library)
                            print(RETURN_TO_MAIN)
                            break

            case "8": # remove book
                return_previous = False
                
                while True:
                    title = input("Enter the book title to be removed: ").strip().title()
                    if is_return_previous(title):
                        return_previous = True
                        break

                    if library.remove_book(title):
                        save_library(library)
                        print(BOOK_REMOVED)

                    else:
                        print(INVALID_BOOK_TITLE)
                        continue

            case "9": # exit program
                save_library(library)
                print("Goodbye!")
                break

if __name__ == "__main__":
    main()