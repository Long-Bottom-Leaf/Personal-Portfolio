# Temporary storage for fitness data

from models import user_profile as profile
from models import workout as workout
from models import goal as goal

class FitnessTracker:

    def __init__(self, profile=None):
        self.profile = profile
        self.workouts = []
        self.goals = []

    def set_profile(self, profile):
        self.profile = profile

    def add_workout(self, workout):
        self.workouts.append(workout)

    def add_goal(self, goal):
        self.goals.append(goal)

    def view_profile(self):
        if self.profile is None:
            print("No profile set.")
            return
        
        print(self.profile)
    
    def view_workouts(self):
        if not self.workouts:
            print("No workouts logged.")
            return
        
        for index, workout in enumerate(self.workouts, start=1):
            print(f"\nWorkout #{index}")
            print(workout)

    def view_goals(self):
        if not self.goals:
            print("No goals set.")
            return
        
        for index, goal in enumerate(self.goals, start=1):
            print(f"\nGoal #{index}")
            print(goal)