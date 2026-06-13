# Temporary storage for fitness data

from models import user_profile as profile
from models import workout as workout
from models import goal as goal

class FitnessTracker:

    def __init__(self, profile=None):
        self.profile = profile
        self.workouts = []
        self.goals = []

# Profile Management
    def set_profile(self, profile):
        self.profile = profile

    def view_profile(self):
        if self.profile is None:
            print("No profile set.")
            return
        
        print(self.profile)

    def clear_profile(self):
        self.profile = None
        print("Profile cleared.")

# Workout Management
    def add_workout(self, workout):
        self.workouts.append(workout)
    
    def view_workouts(self):
        if not self.workouts:
            print("No workouts logged.")
            return
        
        for index, workout in enumerate(self.workouts, start=1):
            print(f"\nWorkout #{index}")
            print(workout)

    def workout_summary(self):
        if not self.workouts:
            print("No workouts logged.")
            return
        
        total_duration = sum(workout.duration for workout in self.workouts)
        total_calories = sum(workout.calories_burned for workout in self.workouts)

        print(f"Total Workouts: {len(self.workouts)}")
        print(f"Total Duration: {total_duration} minutes")
        print(f"Total Calories Burned: {total_calories} kcal")

    def clear_workouts(self):
        self.workouts.clear()
        print("All workouts cleared.")

# Goal Management
    def add_goal(self, goal):
        self.goals.append(goal)

    def view_goals(self):
        if not self.goals:
            print("No goals set.")
            return
        
        for index, goal in enumerate(self.goals, start=1):
            print(f"\nGoal #{index}")
            print(goal) 

    def clear_goals(self):
        self.goals.clear()
        print("All goals cleared.")