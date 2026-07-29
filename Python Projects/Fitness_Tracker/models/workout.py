# Workout model

from datetime import date

class Workout:

    def __init__(self, workout_type, duration, intensity, calories, notes):

        self.workout_date = date.today()
        self.workout_type = workout_type
        self.workout_duration = duration
        self.workout_intensity = intensity
        self.calories_burned = calories
        self.notes = notes

    def __str__(self):

        return (
            f"Date: {self.workout_date},\n"
            f"Type: {self.workout_type}, "
            f"Duration: {self.workout_duration} min,\n"
            f"Intensity: {self.workout_intensity},\n"
            f"Calories: {self.calories_burned},\n"
            f"Notes: {self.notes}"
        )