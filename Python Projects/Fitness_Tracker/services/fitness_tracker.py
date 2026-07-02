# Temporary storage for fitness data

class FitnessTracker:

    def __init__(self, user_profile=None):
        self.profile = user_profile
        self.workouts = []
        self.goals = []

# Profile Management
    def set_profile(self, user_profile):
        self.profile = user_profile
        print("Profile saved!")

    def view_profile(self):
        if self.profile is None:
            print("No profile set.")
            return
        
        print("Profile loaded!")
        print(self.profile)

    def clear_profile(self):
        print("Clearing profile...")

        self.profile = None
        print("Profile cleared.")

# Workout Management
    def add_workout(self, workout):
        self.workouts.append(workout)
        print("Workout added!")
    
    def view_workouts(self):
        if not self.workouts:
            print("No workouts logged.")
            return
        
        for index, workout in enumerate(self.workouts, start=1):
            print("Loading workouts...")
            print(f"\nWorkout #{index}")
            print(workout)

    def workout_summary(self):
        if not self.workouts:
            print("No workouts logged.")
            return
        
        total_duration = sum(workout.workout_duration for workout in self.workouts)
        total_calories = sum(workout.calories_burned for workout in self.workouts)

        print("Loading workout summary...")
        print(f"Total Workouts: {len(self.workouts)}")
        print(f"Total Duration: {total_duration} minutes")
        print(f"Total Calories Burned: {total_calories} kcal")

    def clear_workouts(self):
        print("Clearing workouts...")
        self.workouts.clear()
        print("All workouts cleared.")

# Goal Management
    def add_goal(self, goal):
        self.goals.append(goal)
        print("Goal saved!")

    def view_goals(self):
        if not self.goals:
            print("No goals set.")
            return
        
        print("Loading goals...")
        for index, goal in enumerate(self.goals, start=1):
            print(f"\nGoal #{index}")
            print(goal) 

    def clear_goals(self):
        self.goals.clear()
        print("All goals cleared.")