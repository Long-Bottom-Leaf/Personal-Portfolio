# Test fitness tracker service

import sys
import os
import unittest

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from services.fitness_tracker import FitnessTracker
from models.user_profile import UserProfile
from models.workout import Workout
from models.goal import Goal

class TestFitnessTracker(unittest.TestCase):

    def setUp(self):
        self.fitness_tracker = FitnessTracker()

    # Profile tests
    def test_set_and_view_profile(self):
        user_profile1 = UserProfile("John French", 180, "lbs")

        self.fitness_tracker.set_profile(user_profile1)
        self.fitness_tracker.view_profile()

        self.assertEqual(self.fitness_tracker.profile.user_name, "John French")
        self.assertEqual(self.fitness_tracker.profile.user_weight, 180)
        self.assertEqual(self.fitness_tracker.profile.weight_unit, "lbs")

    def test_clear_profile(self):
        user_profile2 = UserProfile("John French", 180, "lbs")

        self.fitness_tracker.set_profile(user_profile2)
        self.fitness_tracker.clear_profile()

        self.assertIsNone(self.fitness_tracker.profile)

    # Workout tests
    def test_add_and_view_workouts(self):
        workout1 = Workout("Running", 30, "medium", 300, "Morning run")
        workout2 = Workout("Cycling", 45, "high", 400, "Evening ride")

        self.fitness_tracker.add_workout(workout1)
        self.fitness_tracker.add_workout(workout2)
        self.fitness_tracker.view_workouts()

        self.assertEqual(len(self.fitness_tracker.workouts), 2)

    def test_workout_summary(self):
        workout1 = Workout("Running", 30, "medium", 300, "Morning run")
        workout2 = Workout("Cycling", 45, "high", 400, "Evening ride")

        self.fitness_tracker.add_workout(workout1)
        self.fitness_tracker.add_workout(workout2)
        self.fitness_tracker.view_workouts()

        self.fitness_tracker.workout_summary()

        total_duration = sum(
            workout.workout_duration for workout in self.fitness_tracker.workouts
        )

        self.assertEqual(total_duration, 75)

    def test_clear_workouts(self):
        workout1 = Workout("Running", 30, "medium", 300, "Morning run")
        workout2 = Workout("Cycling", 45, "high", 400, "Evening ride")

        self.fitness_tracker.add_workout(workout1)
        self.fitness_tracker.add_workout(workout2)
        self.fitness_tracker.clear_workouts()

        self.assertEqual(len(self.fitness_tracker.workouts), 0)

    # Goal tests
    def test_add_and_view_goals(self):
        goal1 = Goal(3, 150, 2000, "Swimming")
        goal2 = Goal(4, 200, 2500, "Running")

        self.fitness_tracker.add_goal(goal1)
        self.fitness_tracker.add_goal(goal2)
        self.fitness_tracker.view_goals()

        self.assertEqual(len(self.fitness_tracker.goals), 2)

    def test_clear_goals(self):
        goal1 = Goal(3, 150, 2000, "Swimming")
        goal2 = Goal(4, 200, 2500, "Running")

        self.fitness_tracker.add_goal(goal1)
        self.fitness_tracker.add_goal(goal2)
        self.fitness_tracker.clear_goals()

        self.assertEqual(len(self.fitness_tracker.goals), 0)

if __name__ == '__main__':
    unittest.main()