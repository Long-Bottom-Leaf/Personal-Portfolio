# Test workout date sorter

import sys
import os
import unittest
from datetime import date

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from models.workout import Workout
from utils.sorter import sort_workouts_by_date

class TestWorkoutDateSort(unittest.TestCase):

    def test_sort_newest_first(self):
        workout1 = Workout("Running", 30, "medium", 300, "Morning run")
        workout2 = Workout("Cycling", 45, "high", 500, "After work cycling")
        workout3 = Workout("Swimming", 60, "low", 400, "Light swim with friends")

        workout1.workout_date = date(2026, 6, 20)
        workout2.workout_date = date(2026, 6, 30)
        workout3.workout_date = date(2026, 6, 25)

        workouts = [workout1, workout2, workout3]

        sorted_workouts = sort_workouts_by_date(workouts)

        self.assertEqual(
            [workout.workout_date for workout in sorted_workouts],
            [
                date(2026, 6, 30),
                date(2026, 6, 25),
                date(2026, 6, 20)

            ]
        )

    def test_sort_oldest_first(self):
        workout1 = Workout("Running", 30, "medium", 300, "Morning run")
        workout2 = Workout("Cycling", 45, "high", 500, "After work cycling")
        workout3 = Workout("Swimming", 60, "low", 400, "Light swim with friends")

        workout1.workout_date = date(2026, 6, 20)
        workout2.workout_date = date(2026, 6, 30)
        workout3.workout_date = date(2026, 6, 25)

        workouts = [workout1, workout2, workout3]

        sorted_workouts = sort_workouts_by_date(
            workouts,
            newest_first=False
        )

        self.assertEqual(
            [workout.workout_date for workout in sorted_workouts],
            [
                date(2026, 6, 20),
                date(2026, 6, 25),
                date(2026, 6, 30)

            ]
        )

if __name__ == "__main__":
    unittest.main()
        