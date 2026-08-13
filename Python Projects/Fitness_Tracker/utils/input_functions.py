# Input functions for main.py

from utils.error_messages import (
    INVALID_NAME,
    INVALID_GOAL_COUNT,
    INVALID_WEIGHT_UNIT,
    INVALID_INTENSITY,
    INVALID_WORKOUT_TYPE,
    INVALID_INPUT
)

from utils.validators import (
    VALID_ACTIVITIES,
    validate_positive_number,
    validate_goal_count,
    validate_weight_unit,
    validate_intensity,
    validate_activity,
    validate_name
)

# Validations
def get_valid_name():
    while True:
        name = input("Enter your name: ").strip()

        if validate_name(name):
            return name

        print(INVALID_NAME)

def get_valid_number(prompt, error_message):
    while True:
        value = input(prompt)

        if validate_positive_number(value):
            return float(value)

        print(error_message)

def get_valid_goal_count(prompt):
    while True:
        value = input(prompt)

        if validate_goal_count(value):
            return int(value)
        
        else:
            print(INVALID_GOAL_COUNT)

def get_valid_weight_unit():
    while True:
        weight_unit = input("Enter weight unit (kgs/lbs): ")

        if validate_weight_unit(weight_unit):
            return weight_unit.strip().lower()
        
        else:
            print(INVALID_WEIGHT_UNIT)

def get_valid_intensity():
    while True:
        intensity = input("Enter intensity (low/medium/high): ")

        if validate_intensity(intensity):
            return intensity.strip().lower()
        
        else:
            print(INVALID_INTENSITY)
        
def get_valid_activity():
    while True:
        print("\nWorkout Types:")

        for code, activity in VALID_ACTIVITIES.items():
            print(f"{code} - {activity}")

        activity_code = input("Enter workout type: ")

        if validate_activity(activity_code):
            return VALID_ACTIVITIES[activity_code.strip().upper()]
        
        else:
            print(INVALID_WORKOUT_TYPE)

# Confirmation helper
def ask_yes_no(prompt):
    while True:
        reply = input(f"{prompt} (y/n): ").strip().lower()
        
        if reply in ['yes', 'y']:
            return True
        
        elif reply in ['no', 'n']:
            return False
        
        print(INVALID_INPUT)