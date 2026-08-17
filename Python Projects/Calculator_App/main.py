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

        numbers = input("Enter numbers separated by spaces: ")
        numbers = [float(number) for number in numbers.split()]

        if choice == "1":
            result = add(*numbers)
            print(f"{numbers[0]} + {numbers[1]} = {result}")

        elif choice == "2":
            result = subtract(numbers[0], numbers[1])
            print(f"{numbers[0]} - {numbers[1]} = {result}")

        elif choice == "3":
            result = multiply(numbers[0], numbers[1])
            print(f"{numbers[0]} x {numbers[1]} = {result}")

        elif choice == "4":
            result = divide(numbers[0], numbers[1])
            print(f"{numbers[0]} / {numbers[1]} = {result}")

if __name__ == "__main__":
    main()