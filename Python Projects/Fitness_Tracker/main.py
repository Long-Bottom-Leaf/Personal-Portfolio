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

# Validations
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

def get_valid_intensity():
    while True:
        intensity = input("Enter intensity (low/medium/hight): ")

        if validate_intensity(intensity):
            return intensity.strip().lower()
        
        else:
            return("Invalid intensity. Please enter low, medium, or hight!")
        
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

# Create profile
def create_profile(fitness_tracker):
    name = input("Enter your name: ")
    weight = get_valide_number("Enter your weight: ")
    weight_unit = get_valid_weight_unit()

    profile = UserProfile(name, weight, weight_unit)
    fitness_tracker.set_profile(profile)

    print("Profile created successfully!")

# Add workout
def add_workout(fitness_tracker):
    if fitness_tracker.profile is None:
        print("Pease create a profile first!")
        
        return
    
    workout_type = get_valid_activity()
    duration = get_valide_number("Enter workout duration (in minutes): ")
    intensity = get_valid_intensity()
    notes = input("Enter workout notes here: ")

    calories_burned = calculate_calories(
        workout_type,
        intensity,
        FitnessTracker.profile.user_weight,
        duration,
        weight_unit
    )

# Create/view goal

# Menu
def main():
    
if __name__ == "__main__":
    main()