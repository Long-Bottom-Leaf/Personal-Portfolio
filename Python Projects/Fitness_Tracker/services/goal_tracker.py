class GoalTracker:

    def __init__(self, workouts, goals):
        self.workouts = workouts
        self.goals = goals

    def show_goal_progress(self):

        if not self.goal:
            print("No goal set.")
            return

        if not self.workout:
            print("No workout logged.")
            return

        total_workouts = len(self.workout)