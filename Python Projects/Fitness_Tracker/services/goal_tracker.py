class goal_tracker:

    def __init__(self, workout, goal):
        self.workout = workout
        self.goal = goal

    def show_goal_progress(self):

        if not self.goal:
            print("No goal set.")
            return

        if not self.workout:
            print("No workout logged.")
            return

        total_workouts = len(self.workout)