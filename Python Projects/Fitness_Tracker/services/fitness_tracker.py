# Temporary storage for fitness data

from utils.loading_bar import loading_bar
from services.actions import get_favorite_workout

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
            print("\nNo profile set.\n")
            return
        
        loading_bar("\nLoading profile...\n", total=20)
        print(self.profile)

    def clear_profile(self):
        print("\nClearing profile...\n")

        self.profile = None

# Workout Management
    def add_workout(self, workout):
        self.workouts.append(workout)
    
    def view_workouts(self):
        if not self.workouts:
            print("\nNo workouts logged.\n")
            return
        
        loading_bar("\nLoading workouts...\n", total=25)
        
        for index, workout in enumerate(self.workouts, start=1):
            print(f"\nWorkout #{index}")
            print(workout)

    def workout_summary(self):
        if not self.workouts:
            print("\nNo workouts logged.\n")
            return
        
        total_duration = sum(workout.workout_duration for workout in self.workouts)
        total_calories = sum(workout.calories_burned for workout in self.workouts)

        average_duration = round(total_duration / len(self.workouts), 1)
        average_calories = round(total_calories / len(self.workouts), 1)

        workout_type, count = self.get_favorite_workout()

        loading_bar("\nLoading workout summary...\n", total=20)
        print("==== Workout Summary ====")
        print(f"Total Workouts: {len(self.workouts)}")
        print(f"Total Duration: {total_duration} minutes")
        print(f"Total Calories Burned: {total_calories} kcal")
        print(f"Average Duration: {average_duration}")
        print(f"Average Calories Burned: {average_calories}")
        print(f"Favorite Workout: {workout_type} ({count} workouts)")

    def clear_workouts(self):
        loading_bar("\nClearing workouts...\n", total=15)
        self.workouts.clear()

# Goal Management
    def add_goal(self, goal):
        self.goals.append(goal)

    def view_goals(self):
        if not self.goals:
            print("\nNo goals set.\n")
            return
        
        loading_bar("\nLoading goals...\n", total=20)
        for index, goal in enumerate(self.goals, start=1):
            print(f"\nGoal #{index}")
            print(goal)

    def clear_goals(self):
        loading_bar("Clearing goals...\n", total=15)
        self.goals.clear()