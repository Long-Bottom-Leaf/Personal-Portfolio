# Main Fitness Tracker Application

import os
import sys
sys.path.insert(0, os.path.dirname(__file__))

from services.fitness_tracker import FitnessTracker
from services.actions import (
    create_profile,
    add_workout,
    create_goal,
    view_goal_progress
)
from services.csv_exporter import export_workouts_to_csv
from storage.data_manager import DataManager

from utils.input_functions import ask_yes_no
from utils.validators import validate_menu_choice
from utils.error_messages import (
    INVALID_MENU_CHOICE,
    INVALID_SORT,
    ACTION_CANCELLED
)
from utils.success_messages import (
    PROFILE_SAVED,
    PROFILE_LOADED,
    PROFILE_CLEARED,
    WORKOUT_ADDED,
    ALL_WORKOUT_CLEARED,
    GOAL_SAVED,
    GOALS_CLEARED
)

# Menu
def display_menu():
    print("\n===== Fitness Tracker Menu =====")

    print("\nProfile")
    print("1. Create Profile")
    print("2. View Profile")
    print("3. Clear Profile")

    print("\nWorkouts")
    print("4. Add Workout")
    print("5. View Workouts")
    print("6. Workout Summary")
    print("7. Clear Workouts")

    print("\nGoals")
    print("8. Create Goal")
    print("9. View Goals")
    print("10. View Goal Progress")
    print("11. Clear goals")

    print("\nExport Workouts")
    print("12. Export Workouts to CSV")

    print("13. Exit")

def main():
    fitness_tracker = FitnessTracker()
    data_manager = DataManager()

    # Load saved data
    data_manager.load_tracker(fitness_tracker)

    while True:
        display_menu()

        choice = input("Enter an option: ")

        if not validate_menu_choice(choice, ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13"]):
            print(INVALID_MENU_CHOICE)
            continue

        match choice:
            case "1":
                create_profile(fitness_tracker)
                data_manager.save_tracker(fitness_tracker)
                print(PROFILE_SAVED)

            case "2":
                fitness_tracker.view_profile()
                print(PROFILE_LOADED)

            case "3":
                if ask_yes_no("Are you sure you want to clear your profile?"):
                    fitness_tracker.clear_profile()
                    data_manager.save_tracker(fitness_tracker)
                    print(PROFILE_CLEARED)

                else:
                    print(ACTION_CANCELLED)

            case "4":
                add_workout(fitness_tracker)
                data_manager.save_tracker(fitness_tracker)
                print(WORKOUT_ADDED)

            case "5":
                sort_choice = input(
                    "Sort workouts:\n"
                    "1. Newest to Oldest\n"
                    "2. Oldest to Newest\n"
                    "Choice: "
                ).strip()

                if sort_choice == "1":
                    fitness_tracker.view_workouts(newest_first=True)

                elif sort_choice == "2":
                    fitness_tracker.view_workouts(newest_first=False)

                else:
                    print(INVALID_SORT)
                    fitness_tracker.view_workouts()

            case "6":
                fitness_tracker.workout_summary()

            case "7":
                if ask_yes_no("Are you sure you want to clear your workouts?"):
                    fitness_tracker.clear_workouts()
                    data_manager.save_tracker(fitness_tracker)
                    print(ALL_WORKOUT_CLEARED)

                else:
                    print(ACTION_CANCELLED)

            case "8":
                create_goal(fitness_tracker)
                data_manager.save_tracker(fitness_tracker)
                print(GOAL_SAVED)

            case "9":
                fitness_tracker.view_goals()

            case "10":
                view_goal_progress(fitness_tracker)

            case "11":
                if ask_yes_no("Are you sure you want to clear your goals?"):
                    fitness_tracker.clear_goals()
                    print(GOALS_CLEARED)

                else:
                    print(ACTION_CANCELLED)
            
            case "12":
                export_workouts_to_csv(fitness_tracker.workouts)

            case "13":
                print("Goodbye!")
                break
    
if __name__ == "__main__":
    main()