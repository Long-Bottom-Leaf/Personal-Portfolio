# Input functions for main.py

from utils.validators import (
    VALID_ACTIVITIES,
    validate_positive_number,
    validate_goal_count,
    validate_weight_unit,
    validate_intensity,
    validate_activity,
    validate_menu_choice,
    validate_name
)

# Validations
def get_valid_number(prompt):
    while True:
        value = input(prompt)

        if validate_positive_number(value):
            return float(value)
        
        else:
            print("Invalid number. Please enter a positive number!")

def get_valid_goal_count(prompt):
    while True:
        value = input(prompt)

        if validate_goal_count(value):
            return int(value)
        
        else:
            print("Invalid goal count. Please enter 0 or greater!")

def get_valid_weight_unit():
    while True:
        weight_unit = input("Enter weight unit (kgs/lbs): ")

        if validate_weight_unit(weight_unit):
            return weight_unit.strip().lower()
        
        else:
            print("Invalid weight unit. Please enter kgs or lbs!")

def get_valid_intensity():
    while True:
        intensity = input("Enter intensity (low/medium/high): ")

        if validate_intensity(intensity):
            return intensity.strip().lower()
        
        else:
            print("Invalid intensity. Please enter low, medium, or hight!")
        
def get_valid_activity():
    while True:
        print("\nWorkout Types:")

        for code, activity in VALID_ACTIVITIES.items():
            print(f"{code} - {activity}")

        activity_code = input("Enter workout type: ")

        if validate_activity(activity_code):
            return VALID_ACTIVITIES[activity_code.strip().upper()]
        
        else:
            print("Invalid workout type!")

# Confirmation helper
def ask_yes_no(prompt):
    while True:
        reply = input(f"{prompt} (y/n): ").strip().lower()
        
        if reply in ['yes', 'y']:
            return True
        
        elif reply in ['no', 'n']:
            return False
        
        print("Invalid input. Please enter 'y' or 'n'.")