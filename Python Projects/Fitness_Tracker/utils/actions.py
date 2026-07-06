# Action functions for main.py

from models.user_profile import UserProfile
from models.workout import Workout
from models.goal import Goal

from services.calories_calculator import calculate_calories
from services.goal_tracker import GoalTracker
from utils.input_functions import (
    get_valid_number,
    get_valid_goal_count,
    get_valid_weight_unit,
    get_valid_intensity,
    get_valid_activity,
    ask_yes_no
)
from utils.validators import validate_name

# Create profile
def create_profile(fitness_tracker):
    while True:
        name = input("Enter your name: ").strip()

        if validate_name(name):
            break

        print("Invalid name! Use 3-50 letters, spaces, hyphens, or apostrophes.")

    weight = get_valid_number("Enter your weight: ")
    weight_unit = get_valid_weight_unit()

    profile = UserProfile(name, weight, weight_unit)
    fitness_tracker.set_profile(profile)

# Add workout
def add_workout(fitness_tracker):
    if fitness_tracker.profile is None:
        print("Please create a profile first!")
        
        return
    
    workout_type = get_valid_activity()
    duration = get_valid_number("Enter workout duration (in minutes): ")
    intensity = get_valid_intensity()
    notes = input("Enter workout notes here: ")

    calories = calculate_calories(
        workout_type,
        intensity,
        fitness_tracker.profile.user_weight,
        duration,
        fitness_tracker.profile.weight_unit
    )

    workout = Workout(
        workout_type,
        duration,
        intensity,
        calories,
        notes
    )

    fitness_tracker.add_workout(workout)

# Create/view goal
def create_goal(fitness_tracker):
    weekly_workout_count = get_valid_goal_count("Enter weekly workout count goal: ")
    weekly_duration = get_valid_number("Enter weekly workout duration goal: ")
    weekly_calories = get_valid_number("Enter target calorie goal: ")
    workout_type_goal = get_valid_activity()

    goal = Goal(
        weekly_workout_count,
        weekly_duration,
        weekly_calories,
        workout_type_goal
    )

    fitness_tracker.add_goal(goal)

def view_goal_progress(fitness_tracker):
    goal_tracker = GoalTracker(
        fitness_tracker.workouts,
        fitness_tracker.goals
    )

    goal_tracker.show_goal_progress()