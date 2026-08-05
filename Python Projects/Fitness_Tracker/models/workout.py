# Workout model

from datetime import date

class Workout:

    def __init__(
        self,
        workout_type,
        duration,
        intensity,
        calories,
        notes,
        workout_date=None
    ):

        self.workout_date = workout_date or date.today()
        self.workout_type = workout_type
        self.workout_duration = duration
        self.workout_intensity = intensity
        self.calories_burned = calories
        self.notes = notes

    def __str__(self):

        return (
            f"Date: {self.workout_date}\n"
            f"Type: {self.workout_type}\n"
            f"Duration: {self.workout_duration} minutes\n"
            f"Intensity: {self.workout_intensity}\n"
            f"Calories Burned: {self.calories_burned} kcal\n"
            f"Notes: {self.notes}"
        )