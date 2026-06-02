# Validators for user input

VALID_INTENSITIES = ['low', 'medium', 'high']

VALID_WEIGHT_UNITS = ['kg', 'lb']

VALID_ACTIVITIES = {
    "C" : "Cardio",
    "R" : "Running",
    "W" : "Walking",
    "S" : "Strength",
    "Y" : "Cycling",
    "O" : "Other"
}

def validate_positive_number(value):
    """ Validates weight, duration, calories, and goal value inputs. """

    try:
        value = float(value)
        return value > 0
    
    except ValueError:
        return False
    
def validate_goal_count(value):
    """ Goal count can be 0 or greater. """

    try:
        value = float(value)
        return value >= 0
    
    except ValueError:
        return False
    
def validate_weight_unit(weight_unit):
    """ Validates weight unit input. """

    return weight_unit in VALID_WEIGHT_UNITS

def validate_intensity(intensity):

    return intensity.lower() in VALID_INTENSITIES


def validate_activity(activity):

    return activity.upper() in VALID_ACTIVITIES


def validate_menu_choice(choice, valid_choices):

    return choice in valid_choices