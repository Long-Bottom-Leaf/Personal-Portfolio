# Fitness Goal model

class Goal:

    def __init__(self, weekly_workout_count, weekly_duration, weekly_calories, workout_type_goal):

        self.weekly_workout_count = weekly_workout_count
        self.weekly_duration = weekly_duration
        self.weekly_calories = weekly_calories
        self.workout_type_goal = workout_type_goal

    def __str__(self):

        return (
            f"Workout Count: {self.weekly_workout_count}, "
            f"Weekly Duration: {self.weekly_duration} min, "
            f"Weekly Calories: {self.weekly_calories} kcal, "
            f"Workout Type Goal: {self.workout_type_goal}"
        )