# Temporary storage for fitness data

from utils.loading_bar import loading_bar
from collections import Counter
from utils.sorter import sort_workouts_by_date

from utils.error_messages import (
    NO_PROFILE,
    NO_WORKOUT,
    NO_GOAL
)

class FitnessTracker:

    def __init__(self, user_profile=None):
        self.profile = user_profile
        self.workouts = []
        self.goals = []

# Profile Management
    def set_profile(self, user_profile):
        self.profile = user_profile

    def view_profile(self):
        if self.profile is None:
            print(NO_PROFILE)
            return
        
        loading_bar("\nLoading profile...\n", total=20)
        print(self.profile)

    def clear_profile(self):
        print("\nClearing profile...\n")

        self.profile = None

# Workout Management
    def add_workout(self, workout):
        self.workouts.append(workout)
    
    def view_workouts(self, newest_first=True):
        if not self.workouts:
            print(NO_WORKOUT)
            return
        
        workouts = sort_workouts_by_date(self.workouts, newest_first=newest_first)
        
        loading_bar("\nLoading workouts...\n", total=25)
        
        for index, workout in enumerate(workouts, start=1):
            print("=" * 40)
            print(f"Workout #{index}")
            print("-" * 40)
            print(workout)
            print("=" * 40)

    def get_favorite_workout(self):
        if not self.workouts:
            return None

        workout_counts = Counter(
            workout.workout_type
            for workout in self.workouts
        )

        return workout_counts.most_common(1)[0]
    
    def get_longest_workout(self):
        if not self.workouts:
            return None

        return max(
            self.workouts,
            key=lambda workout: workout.workout_duration
        )
    
    def get_highest_calorie_workout(self):
        if not self.workouts:
            return None

        return max(
            self.workouts,
            key=lambda workout: workout.calories_burned
        )

    def workout_summary(self):
        if not self.workouts:
            print(NO_WORKOUT)
            return
        
        total_duration = sum(workout.workout_duration for workout in self.workouts)
        total_calories = sum(workout.calories_burned for workout in self.workouts)

        average_duration = round(total_duration / len(self.workouts), 1)
        average_calories = round(total_calories / len(self.workouts), 1)

        favorite_type, favorite_count = self.get_favorite_workout()

        longest = self.get_longest_workout()
        highest = self.get_highest_calorie_workout()

        loading_bar("\nLoading workout summary...\n", total=20)
        print("==== Workout Summary ====")
        print(f"Total Workouts: {len(self.workouts)}")
        print(f"Total Duration: {total_duration} minutes")
        print(f"Total Calories Burned: {total_calories} kcal\n")

        print(f"Average Duration: {average_duration} minutes")
        print(f"Average Calories Burned: {average_calories} kcal\n")

        print(f"Favorite Workout: {favorite_type} ({favorite_count} workouts)")
        print(
            f"Longest Workout: "
            f"{longest.workout_type} ({longest.workout_duration} minutes)"
        )
        print(
            f"Highest Calorie Workout: "
            f"{highest.workout_type} ({highest.calories_burned} kcal)"
        )

    def clear_workouts(self):
        loading_bar("\nClearing workouts...\n", total=15)
        self.workouts.clear()

# Goal Management
    def add_goal(self, goal):
        self.goals.append(goal)

    def view_goals(self):
        if not self.goals:
            print(NO_GOAL)
            return
        
        loading_bar("\nLoading goals...\n", total=20)
        for index, goal in enumerate(self.goals, start=1):
            print(f"\nGoal #{index}")
            print(goal)

    def clear_goals(self):
        loading_bar("Clearing goals...\n", total=15)
        self.goals.clear()