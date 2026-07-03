# Temporary storage for fitness data

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
            print("\nNo profile set.")
            return
        
        print(self.profile)

    def clear_profile(self):
        print("\nClearing profile...")

        self.profile = None

# Workout Management
    def add_workout(self, workout):
        self.workouts.append(workout)
    
    def view_workouts(self):
        if not self.workouts:
            print("\nNo workouts logged.")
            return
        
        for index, workout in enumerate(self.workouts, start=1):
            print("\nLoading workouts...")
            print(f"\nWorkout #{index}")
            print(workout)

    def workout_summary(self):
        if not self.workouts:
            print("\nNo workouts logged.")
            return
        
        total_duration = sum(workout.workout_duration for workout in self.workouts)
        total_calories = sum(workout.calories_burned for workout in self.workouts)

        print("\nLoading workout summary...")
        print(f"Total Workouts: {len(self.workouts)}")
        print(f"Total Duration: {total_duration} minutes")
        print(f"Total Calories Burned: {total_calories} kcal")

    def clear_workouts(self):
        print("\nClearing workouts...")
        self.workouts.clear()

# Goal Management
    def add_goal(self, goal):
        self.goals.append(goal)

    def view_goals(self):
        if not self.goals:
            print("\nNo goals set.")
            return
        
        print("\nLoading goals...")
        for index, goal in enumerate(self.goals, start=1):
            print(f"\nGoal #{index}")
            print(goal) 

    def clear_goals(self):
        self.goals.clear()