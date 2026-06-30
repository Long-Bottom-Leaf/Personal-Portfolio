# Main Fitness Tracker Application

from models.user_profile import UserProfile
from models.workout import Workout
from models.goal import Goal

from services.fitness_tracker import FitnessTracker
from services.calories_calculator import calculate_calories
from services.goal_tracker import GoalTracker
from services.csv_exporter import export_workouts_to_csv
from utils.validators import (
    VALID_ACTIVITIES,
    validate_positive_number,
    validate_goal_count,
    validate_weight_unit,
    validate_intensity,
    validate_activity,
    validate_menu_choice
)

def get_valide_number(prompt):
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

def main():
    
if __name__ == "__main__":
    main()