# Main Fitness Tracker Application

from models.user_profile import UserProfile
from models.workout import Workout
from models.goal import Goal

from services.fitness_tracker import FitnessTracker
from services.calories_calculator import calculate_calories
from services.goal_tracker import GoalTracker

def main():
    fitness_tracker = FitnessTracker()

    profile = UserProfile("Stephen", 180, "lbs")
    fitness_tracker.set_profile(profile)

    # Test workout and calories 1
    workout1 = Workout(
        "Running",
        30,
        "medium",
        calories1,
        "Easy test run"
    )

    calories1 = calculate_calories(
        "Running",
        "medium",
        profile.weight,
        30,
        profile.weight_unit
    )

    fitness_tracker.add_workout(workout1)

    # Test workout and calories 2
    workout2 = Workout(
        "Cycling",
        45,
        "high",
        calories2,
        "Intense cycling session"
    )

    calories2 = calculate_calories(
        "Cycling",
        "high",
        profile.weight,
        45,
        profile.weight_unit
    )

    fitness_tracker.add_workout(workout2)

    # Test goal and goal tracking
    goal = Goal(
        4,
        120,
        1500,
        "Running"
    )

    fitness_tracker.add_goal(goal)

    # Print out results
    print("\n=== User Profile ===")
    fitness_tracker.view_profile()

    print("\n=== Workouts ===")
    fitness_tracker.view_workouts()

    print("\n=== Workout Summary ===")
    fitness_tracker.workout_summary()

    print("\n=== Goals ===")
    fitness_tracker.view_goals()

    print("\n=== Goal Progress ===")
    fitness_tracker.view_goal_progress()

if __name__ == "__main__":
    main()