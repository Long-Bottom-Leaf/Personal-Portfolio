# Calculator app

from functions.math_functions import (
    add,
    subtract,
    multiply,
    divide,
    square_root,
    power,
    percent,
    absolute_value,
    simple_interest
)
from utils.validators import (
    validate_menu_choice,
    validate_number,
    validate_minimum_numbers,
    validate_number_count
)
from utils.error_messages import (
    INVALID_CHOICE,
    INVALID_NUMBER,
    DIVIDE_BY_0,
    INVALID_SQUARE_ROOT,
    INVALID_MINIMUM_NUMBERS,
    INVALID_NUMBER_COUNT
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
    print("9. Simple Interest")
    print("10. Exit")

def main():

    while True:
        display_menu()

        choice = input("Enter choice: ")

        if not validate_menu_choice(choice, ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]):
            print(INVALID_CHOICE)
            continue

        if choice == "10":
            print("Goodbye!")
            break

        number_input = input("Enter numbers separated by spaces: ")
        number_strings = number_input.split()

        if not all(validate_number(number) for number in number_strings):
            print(INVALID_NUMBER)
            continue

        numbers = [float(number) for number in number_strings]

        if choice == "1":
            if not validate_minimum_numbers(numbers, 2):
                print(INVALID_MINIMUM_NUMBERS)
                continue

            result = add(*numbers)
            print(f"{numbers[0]} + {numbers[1]} = {result}")

        elif choice == "2":
            if not validate_minimum_numbers(numbers, 2):
                print(INVALID_MINIMUM_NUMBERS)
                continue
            
            result = subtract(*numbers)
            print(f"{numbers[0]} - {numbers[1]} = {result}")

        elif choice == "3":
            if not validate_minimum_numbers(numbers, 2):
                print(INVALID_MINIMUM_NUMBERS)
                continue
            
            result = multiply(*numbers)
            print(f"{numbers[0]} x {numbers[1]} = {result}")

        elif choice == "4":
            try:
                if not validate_minimum_numbers(numbers, 2):
                    print(INVALID_MINIMUM_NUMBERS)
                    continue

                result = divide(*numbers)
                print(f"{numbers[0]} / ... = {result}")

            except ZeroDivisionError:
                print(DIVIDE_BY_0)

        elif choice == "5":
            try:
                if not validate_number_count(numbers, 1):
                    print(INVALID_NUMBER_COUNT)
                    continue

                result = square_root(float(numbers[0]))
                print(f"Square Root: {result}")

            except ValueError:
                print(INVALID_SQUARE_ROOT)

            continue

        elif choice == "6":
            if not validate_number_count(numbers, 2):
                print(INVALID_NUMBER_COUNT)
                continue

            result = power(numbers[0], numbers[1])
            print(f"Result: {result}")

        elif choice == "7":
            if not validate_number_count(numbers, 2):
                print(INVALID_NUMBER_COUNT)
                continue

            result = percent(numbers[0], numbers[1])
            print(f"Result: {result}%")

        elif choice == "8":
            if not validate_number_count(numbers, 1):
                print(INVALID_NUMBER_COUNT)
                continue

            result = absolute_value(numbers[0])
            print(f"Absolute Value: {result}")

        elif choice == "9":
            if not validate_number_count(numbers, 3):
                print(INVALID_NUMBER_COUNT)
                continue

            result = simple

if __name__ == "__main__":
    main()