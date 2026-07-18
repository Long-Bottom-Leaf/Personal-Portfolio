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

from utils.input_functions import ask_yes_no
from utils.validators import validate_menu_choice
from utils.error_messages import (
    INVALID_MENU_CHOICE,
    NO_WORKOUT,
    INVALID_SORT
)
from utils.sorter import sort_workouts_by_date

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
            print(INVALID_MENU_CHOICE)
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
                sort_choice = input("Sort workouts by most recent (1) or oldest (2): ").strip()

                if sort_choice == "1":
                    workouts = sort_workouts_by_date(fitness_tracker.workouts)

                elif sort_choice == "2":
                    workouts = sort_workouts_by_date(
                        fitness_tracker.workouts,
                        newest_first=True
                    )

                else:
                    print(INVALID_SORT)
                    workouts = sort_workouts_by_date(fitness_tracker.workouts)

                if not workouts:
                    print(NO_WORKOUT)

                for idx, workout in enumerate(workouts, start=1):
                    try:
                        line = str(workout)
                    except Exception:
                        line = repr(workout)
                    print(f"{idx}. {line}")

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