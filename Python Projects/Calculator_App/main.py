# Calculator app

from functions.math_functions import (
    add,
    subtract,
    multiply,
    divide,
    square_root,
    power,
    percentage,
    absolute_value
)
from utils.validators import (
    validate_menu_choice,
    validate_number
)
from utils.error_messages import (
    INVALID_CHOICE,
    INVALID_NUMBER,
    DIVIDE_BY_0,
    INVALID_SQUARE_ROOT
)

def display_menu():

    print("\n==== Calculator ====\n")

    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Square Root")
    print("6. Power")
    print("7. Percent")
    print("8. Absolute Value")
    print("9. Exit")

def main():

    while True:
        display_menu()

        choice = input("Enter choice: ")

        if not validate_menu_choice(choice, ["1", "2", "3", "4", "5", "6", "7", "8", "9"]):
            print(INVALID_CHOICE)
            continue

        if choice == "9":
            print("Goodbye!")
            break

        number_input = input("Enter numbers separated by spaces: ")
        number_strings = number_input.split()

        if not all(validate_number(number) for number in number_strings):
            print(INVALID_NUMBER)
            continue

        numbers = [float(number) for number in number_strings]

        if choice == "1":
            result = add(*numbers)
            print(f"{numbers[0]} + {numbers[1]} = {result}")

        elif choice == "2":
            result = subtract(*numbers)
            print(f"{numbers[0]} - {numbers[1]} = {result}")

        elif choice == "3":
            result = multiply(*numbers)
            print(f"{numbers[0]} x {numbers[1]} = {result}")

        elif choice == "4":
            try:
                result = divide(*numbers)
                print(f"{numbers[0]} / ... = {result}")

            except ZeroDivisionError:
                print(DIVIDE_BY_0)

        elif choice == "5":
            try:
                result = square_root(float(numbers[0]))
                print(f"Square Root: {result}")

            except ValueError:
                print(INVALID_SQUARE_ROOT)

            continue

        elif choice == "6":
            result = power(numbers[0], numbers[1])
            print(f"Result: {result}")

        elif choice == "7":
            result = percentage(numbers[0], numbers[1])
            print(f"Result: {result}%")

        elif choice == "8":
            result = absolute_value(numbers[0])
            print(f"Absolute Value: {result}")

if __name__ == "__main__":
    main()