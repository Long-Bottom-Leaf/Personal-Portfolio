# CSV exporter service

import csv
import os

from utils.sorter import sort_workouts_by_date
from utils.error_messages import FILE_SAVE_ERROR

def export_workouts_to_csv(workouts, file_path="exports/workout_history.csv"):

    sorted_workouts = sort_workouts_by_date(workouts)

    os.makedirs(os.path.dirname(file_path), exist_ok=True)

    try:
        with open(file_path, "w", newline="") as file:
            writer = csv.writer(file)

            writer.writerow([
                "Date",
                "Workout Type",
                "Duration",
                "Intensity",
                "Calories Burned",
                "Notes"
            ])

            for workout in sorted_workouts:
                writer.writerow([
                    workout.workout_date,
                    workout.workout_type,
                    workout.workout_duration,
                    workout.workout_intensity,
                    workout.calories_burned,
                    workout.notes
                ])
                
    except OSError:
        print(FILE_SAVE_ERROR)
        return

    print("\nWorkout history successfully exported!")
    print(f"Location: {file_path}")
    print(f"Total workouts exported: {len(sorted_workouts)}")