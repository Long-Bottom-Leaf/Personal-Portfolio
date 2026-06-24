# Test calories calculator service

import sys
import os
import unittest

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from models.workout import Workout
from services.calories_calculator import calculate_calories

class TestCaloriesCalculator(unittest.TestCase):

    def test_calculate_calories_returns_workout_calories(self):
        workout1 = Workout("Running", 30, "medium", 300, "Morning run")
        workout2 = Workout("Walking", 45, "low", 200, "Evening walk")

        calories1 = calculate_calories(workout1)
        self.assertEqual(calories1, 300)

        calories2 = calculate_calories(workout2)
        self.assertEqual(calories2, 200)

if __name__ == "__main__":
    unittest.main()










