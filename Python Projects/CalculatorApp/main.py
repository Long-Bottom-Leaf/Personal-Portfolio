# Calculator app

from functions.math_functions import (
    add,
    subtract,
    multiply,
    divide
)
from utils.validators import validate_menu_choice

def display_menu():

    print("\n==== Calculator ====\n")

    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. End")

def main():

    while True:
        display_menu()

        choice = input("Enter choice(1/2/3/4): ")

        if not validate_menu_choice(choice, [1, 2, 3, 4]):
            

if __name__ == "__main__":
    main()