# Library System Main

from models.book import Book
from models.library import Library
from utils.validators import (
    validate_menu_choice,
)
from utils.error_messages import (
    INVALID_MENU_CHOICE,
)

def display_menu():
    print("\n==== Library Menu ====")

    print("\n1. Add new book")
    print("\n2. View book list")
    print("\n3. View specific book")
    print("\n4. Remove a book")

    print("\n5. Exit")

def main():

    library = Library()

    while True:
        display_menu()

        choice = input("Enter an option: ")

        if not validate_menu_choice(choice, ["1", "2", "3", "4", "5"]):
            print(INVALID_MENU_CHOICE)
            continue

        match choice:
            case "1":
                print("\n==Enter book details==\n")
                title = input("Enter title: ")
                author = input("Enter author: ")
                genre = input("Enter genre: ")
                release_date = input("Enter the release date: ")
                rating = input("Enter rating, if any: ")
                status = input("Enter status (read/unread): ")

                book = Book(
                    title,
                    author,
                    genre,
                    release_date,
                    rating,
                    status
                )

                library.add_book(book)

                print("Book added successfully!")

            case "2":
                print("\n==Library List==")

                library.view_book_list()

            case "3":
                view_book = input("Enter the book title you want to view: ")

                library.view_specific_book(view_book)

            case "4":
                remove_title = input("Enter the book title to be removed: ")

                library.remove_book(remove_title)

            case "5":
                print("Goodbye")
                break

if __name__ == "__main__":
    main()