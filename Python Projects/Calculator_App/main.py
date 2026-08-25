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
    simple_interest,
    compound_interest
)
from utils.validators import (
    validate_menu_choice,
    validate_number,
    validate_minimum_numbers,
    get_valid_number,
    validate_positive_number
)
from utils.error_messages import (
    INVALID_CHOICE,
    INVALID_NUMBER,
    DIVIDE_BY_0,
    INVALID_SQUARE_ROOT,
    INVALID_MINIMUM_NUMBERS,
    INVALID_COMPOUND_PERIOD
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
    print("9. Interest")
    print("10. Exit")

def interest_menu():

    print("\n1. Simple Interest")
    print("2. Compound Interest")

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

        # Addition
        if choice == "1":
            number_input = input("Enter numbers separated by spaces: ")
            number_string = number_input.split()

            if not all(validate_number(number) for number in number_string):
                print(INVALID_NUMBER)
                continue

            numbers = [float(number) for number in number_string]

            if not validate_minimum_numbers(numbers, 2):
                print(INVALID_MINIMUM_NUMBERS)
                continue

            result = add(*numbers)
            expression = " + ".join(str(number) for number in numbers)
            print(f"{expression} = {result}")

        # Subtraction
        elif choice == "2":
            number_input = input("Enter numbers separated by spaces: ")
            number_string = number_input.split()
            
            if not all(validate_number(number) for number in number_string):
                print(INVALID_NUMBER)
                continue
            
            numbers = [float(number) for number in number_string]

            if not validate_minimum_numbers(numbers, 2):
                print(INVALID_MINIMUM_NUMBERS)
                continue
            
            result = subtract(*numbers)
            expression = " - ".join(str(number) for number in numbers)
            print(f"{expression} = {result}")

        # Multiplication
        elif choice == "3":
            number_input = input("Enter numbers separated by spaces: ")
            number_string = number_input.split()
                        
            if not all(validate_number(number) for number in number_string):
                print(INVALID_NUMBER)
                continue
                        
            numbers = [float(number) for number in number_string]
            
            if not validate_minimum_numbers(numbers, 2):
                print(INVALID_MINIMUM_NUMBERS)
                continue
            
            result = multiply(*numbers)
            expression = " x ".join(str(number) for number in numbers)
            print(f"{expression} = {result}")

        # Division
        elif choice == "4":
            number_input = input("Enter numbers separated by spaces: ")
            number_string = number_input.split()
                        
            if not all(validate_number(number) for number in number_string):
                print(INVALID_NUMBER)
                continue
                        
            numbers = [float(number) for number in number_string]
            
            if not validate_minimum_numbers(numbers, 2):
                print(INVALID_MINIMUM_NUMBERS)
                continue
            
            try:
                result = divide(*numbers)
                expression = " / ".join(str(number) for number in numbers)
                print(f"{expression} = {result}")

            except ZeroDivisionError:
                print(DIVIDE_BY_0)

        # Square Root
        elif choice == "5":
            number = get_valid_number("Enter number: ")

            try:
                result = square_root(number)
                print(f"Square Root: {result}")

            except ValueError:
                print(INVALID_SQUARE_ROOT)

        # Exponent
        elif choice == "6":
            base = get_valid_number("Enter base: ")
            exponent = get_valid_number("Enter exponent: ")

            result = power(base, exponent)
            print(f"{base} ^ {exponent} = {result}")

        # Percent
        elif choice == "7":
            number = get_valid_number("Enter number: ")
            percentage = get_valid_number("Enter percentage: ")

            result = percent(number, percentage)
            print(f"{percentage}% of {number} = {result}")

        # Absolute Value
        elif choice == "8":
            number = get_valid_number("Enter number: ")

            result = absolute_value(number)
            print(f"Absolute Value: {result}")

        # Interest
        elif choice == "9":
            interest_menu()

            interest_choice = input("Enter choice: ")
            
            if not validate_menu_choice(interest_choice, ["1", "2"]):
                print(INVALID_CHOICE)
                continue

            principal = get_valid_number("Enter principal: ")
            rate = get_valid_number("Enter interest rate (%): ")
            time = get_valid_number("Enter time (years): ")

            if interest_choice == "1":
                result = simple_interest(principal, rate, time)
                total = principal + result
                
                print(f"Interest Earned: ${result:.2f}")
                print(f"Total Amount: ${total:.2f}")
                
            elif interest_choice == "2":
                compound_period = get_valid_number("Enter compounding periods per year: ")

                if not validate_positive_number(compound_period):
                    print(INVALID_COMPOUND_PERIOD)
                    continue
                
                result = compound_interest(
                    principal,
                    rate,
                    compound_period,
                    time
                )
                
                interest = result - principal
                
                print(f"Interest Earned: ${interest:.2f}")
                print(f"Total Amount: ${result:.2f}")

if __name__ == "__main__":
    main()