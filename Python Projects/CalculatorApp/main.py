# Calculator app

from functions.math_functions import (
    add,
    subtract,
    multiply,
    divide
)
from utils.validators import validate_menu_choice
from utils.error_messages import (
    INVALID_CHOICE
)

def display_menu():

    print("\n==== Calculator ====\n")

    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

def main():

    while True:
        display_menu()

        choice = input("Enter choice(1/2/3/4/5): ")

        if not validate_menu_choice(choice, ["1", "2", "3", "4", "5"]):
            print(INVALID_CHOICE)
            continue

        if choice == "5":
            print("Goodbye!")
            break

        x = float(input("Enter first number: "))
        y = float(input("Enter second number: "))

        if choice == "1":
            print(f"Result: {add(x, y)}")

        elif choice == "2":
            print(f"Result: {subtract(x, y)}")

        elif choice == "3":
            print(f"Result: {multiply(x, y)}")

        elif choice == "4":
            print(f"Result: {divide(x, y)}")

if __name__ == "__main__":
    main()