# Validators for user input

from datetime import datetime
import re

VALID_INTENSITIES = ['low', 'medium', 'high']

VALID_WEIGHT_UNITS = ['kgs', 'lbs']

VALID_ACTIVITIES = {
    "C" : "Cycling",
    "G" : "General Cardio",
    "R" : "Running",
    "S" : "Swimming",
    "W" : "Weights",
    "O" : "Other"
}

def validate_positive_number(value):
    try:
        value = float(value)
        return value > 0
    
    except ValueError:
        return False
    
def validate_goal_count(value):
    try:
        value = float(value)
        return value >= 0
    
    except ValueError:
        return False
    
def validate_weight_unit(weight_unit):
    return weight_unit.strip().lower() in VALID_WEIGHT_UNITS

def validate_intensity(intensity):
    return intensity.strip().lower() in VALID_INTENSITIES


def validate_activity(activity):
    return activity.strip().upper() in VALID_ACTIVITIES


def validate_menu_choice(choice, valid_choices):
    return choice.strip() in valid_choices

def validate_date(date_value):
    try:
        datetime.strptime(date_value, "%Y-%m-%d")
        return True
    
    except ValueError:
        return False
    
def validate_name(name):
    pattern = r"^[A-Za-z][A-Za-z\s'-]{2,49}$"

    return re.fullmatch(pattern, name) is not None