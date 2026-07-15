# Goal tracker service

from utils.error_messages import (
    NO_WORKOUT,
    NO_GOAL
)

class GoalTracker:

    def __init__(self, workouts, goals):
        self.workouts = workouts
        self.goals = goals

    def show_goal_progress(self):

        if not self.goals:
            print(NO_GOAL)
            return

        if not self.workouts:
            print(NO_WORKOUT)
            return

        total_workouts = len(self.workouts)

        total_duration = sum(
            workout.workout_duration
            for workout in self.workouts
        )

        total_calories = sum(
            workout.calories_burned
            for workout in self.workouts
        )

        for index, goal in enumerate(self.goals, start=1):

            matching_type_count = 0

            for workout in self.workouts:
                if workout.workout_type == goal.workout_type_goal:
                    matching_type_count += 1

            print(f"\nGoal Progress #{index}")
            print(f"Workout Count: {total_workouts}/{goal.weekly_workout_count}")
            print(f"Duration: {total_duration}/{goal.weekly_duration} minutes")
            print(f"Calories Burned: {total_calories}/{goal.weekly_calories} kcal")
            print(f"{goal.workout_type_goal} Workouts: {matching_type_count}")