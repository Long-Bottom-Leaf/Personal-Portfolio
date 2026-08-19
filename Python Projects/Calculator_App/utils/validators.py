# Validations for numbers, menu choices, etc

def validate_menu_choice(choice, valid_choices):
    return choice.strip() in valid_choices

def validate_number(value):
    try:
        float(value)
        return True
    
    except ValueError:
        return False

def validate_minimum_numbers(numbers, minimum):
    return len(numbers) >= minimum

def validate_number_count(numbers, required_count):
    return len(numbers) == required_count