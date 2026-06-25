# Test calories calculator service

import sys
import os
import unittest

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from services.calories_calculator import calculate_calories

class TestCaloriesCalculator(unittest.TestCase):

    def test_calculate_calories_running_lbs(self):
        calories1 = calculate_calories(
            "Running",
            "medium",
            180,
            30,
            "lbs"
        )

        self.assertEqual(calories1, 400)

    def test_calculate_cycling_calories_lbs(self):
        calories2 = calculate_calories(
            "Cycling",
            "high",
            180,
            45,
            "lbs"
        )

        self.assertEqual(calories2, 612)

    def test_swimming_low_kgs(self):
        calories = calculate_calories(
            "Swimming",
            "low",
            80,
            60,
            "kgs"
        )

        self.assertEqual(calories, 464)

if __name__ == "__main__":
    unittest.main()










