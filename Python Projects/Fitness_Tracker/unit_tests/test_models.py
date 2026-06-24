# Test program models
import sys
import os
import unittest

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from models.user_profile import UserProfile
from models.workout import Workout
from models.goal import Goal

# User Profile
class TestUserProfile(unittest.TestCase):

    def test_user_profile_creation(self):
        user_profile = UserProfile("John French", 180, "lbs")

        self.assertEqual(user_profile.user_name, "John French")
        self.assertEqual(user_profile.user_weight, 180)
        self.assertEqual(user_profile.weight_unit, "lbs")

# Workout
class TestWorkout(unittest.TestCase):

    def test_workout_creation(self):
        workout = Workout("Running", 30, "medium", 300, "Morning run")

        self.assertEqual(workout.workout_type, "Running")
        self.assertEqual(workout.workout_duration, 30)
        self.assertEqual(workout.workout_intensity, "medium")
        self.assertEqual(workout.calories_burned, 300)
        self.assertEqual(workout.notes, "Morning run")

# Goal
class TestGoal(unittest.TestCase):

    def test_goal_creation(self):
        goal = Goal(3, 150, 2000, "Swimming")

        self.assertEqual(goal.weekly_workout_count, 3)
        self.assertEqual(goal.weekly_duration, 150)
        self.assertEqual(goal.weekly_calories, 2000)
        self.assertEqual(goal.workout_type_goal, "Swimming")

if __name__ == '__main__':
    unittest.main()