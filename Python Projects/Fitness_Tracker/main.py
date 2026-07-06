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

# Menu
def display_menu():
    print("\n===== Fitness Tracker Menu =====")
    print("1. Create Profile")
    print("2. View Profile")
    print("3. Clear Profile")
    print("4. Add Workout")
    print("5. View Workouts")
    print("6. Workout Summary")
    print("7. Clear Workouts")
    print("8. Create Goal")
    print("9. View Goals")
    print("10. View Goal Progress")
    print("11. Clear goals")
    print("12. Export Workouts to CSV")
    print("13. Exit")

def main():
    fitness_tracker = FitnessTracker()

    while True:
        display_menu()

        choice = input("Enter an option: ")

        if not validate_menu_choice(choice, ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13"]):
            print("Invalid choice, please enter a valid choice!")
            continue

        match choice:
            case "1":
                create_profile(fitness_tracker)
                print("\nProfile saved!")

            case "2":
                fitness_tracker.view_profile()
                print("\nProfile loaded!")

            case "3":
                if ask_yes_no("Are you sure you want to clear your profile?"):
                    fitness_tracker.clear_profile()
                    print("\nProfile cleared.")

                else:
                    print("\nAction cancelled!")

            case "4":
                add_workout(fitness_tracker)
                print("\nWorkout added!")

            case "5":
                fitness_tracker.view_workouts()

            case "6":
                fitness_tracker.workout_summary()

            case "7":
                if ask_yes_no("Are you sure you want to clear your workouts?"):
                    fitness_tracker.clear_workouts()
                    print("\nAll workouts cleared.")

                else:
                    print("\nAction cancelled!")

            case "8":
                create_goal(fitness_tracker)
                print("\nGoal saved!")

            case "9":
                fitness_tracker.view_goals()

            case "10":
                view_goal_progress(fitness_tracker)

            case "11":
                if ask_yes_no("Are you sure you want to clear your goals?"):
                    fitness_tracker.clear_goals()
                    print("\nAll goals cleared.")

                else:
                    print("\nAction cancelled!")
            
            case "12":
                export_workouts_to_csv(fitness_tracker.workouts)

            case "13":
                print("Goodbye!")

                break
    
if __name__ == "__main__":
    main()