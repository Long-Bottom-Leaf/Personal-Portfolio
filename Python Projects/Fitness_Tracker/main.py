# Main Fitness Tracker Application

from models.user_profile import UserProfile
from models.workout import Workout
from models.goal import Goal
from services.fitness_tracker import FitnessTracker

def main():
    fitness_tracker = FitnessTracker()

    profile = UserProfile("Stephen", 180, "lbs")
    fitness_tracker.set_profile(profile)

    workout1 = Workout(
        "Running",
        30,
        "medium",
        250,
        "Easy test run"
    )

    workout2 = Workout(
        "Weights",
        45,
        "high",
        400,
        "Upper body workout"
    )

    fitness_tracker.add_workout(workout1)
    fitness_tracker.add_workout(workout2)

    goal = Goal(
        4,
        180,
        1500,
        "Running"
    )

    fitness_tracker.add_goal(goal)

    print("\n=== Profile ===")
    fitness_tracker.view_profile()

    print("\n=== Workouts ===")
    fitness_tracker.view_workouts()

    print("\n=== Goals ===")
    fitness_tracker.view_goals()


if __name__ == "__main__":
    main()