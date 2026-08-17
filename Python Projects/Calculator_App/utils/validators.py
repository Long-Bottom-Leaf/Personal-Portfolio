# Validations for numbers, menu choices, etc

def validate_menu_choice(choice, valid_choices):
    return choice.strip() in valid_choices

def validate_number(value):
    try:
        float(value)
        return True
    
    except ValueError:
        return False