# Library System Main

import os
import sys
sys.path.insert(0, os.path.dirname(__file__))

from utils.validators import (
    validate_menu_choice,
)
from utils.error_messages import (
    INVALID_MENU_CHOICE,
)

def display_menu():
    print("\n==== Library Menu ====")

    print("\n1. Add new book")
    print("\n2. View books")
    print("\n3. Remove a book")
    print("\n4. ")

    print("\n5. Exit")

def main():

    while True:
        display_menu()

        choice = input("Enter an option: ")

        if not validate_menu_choice(choice, ["1", "2", "3", "4", "5"]):
            print(INVALID_MENU_CHOICE)

if __name__ == "__main__":
    main()