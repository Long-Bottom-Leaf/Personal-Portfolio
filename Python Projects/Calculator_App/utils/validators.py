# Validations for numbers, menu choices, etc

from utils.error_messages import INVALID_NUMBER

def validate_menu_choice(choice, valid_choices):
    return choice.strip() in valid_choices

def validate_number(value):
    try:
        float(value)
        return True
    
    except ValueError:
        return False

def validate_positive_number(number):
    return number > 0

def validate_minimum_numbers(numbers, minimum):
    return len(numbers) >= minimum

def get_valid_number(prompt):
    while True:
        value = input(prompt)

        if validate_number(value):
            return float(value)

        print(INVALID_NUMBER)

def get_valid_numbers(prompt):
    while True:
        number_input = input(prompt)
        number_strings = number_input.split()

        if all(validate_number(number) for number in number_strings):
            return [float(number) for number in number_strings]

        print(INVALID_NUMBER)