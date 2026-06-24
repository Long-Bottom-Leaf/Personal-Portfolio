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

    # Profile tests
        def setUp(self):
            self.fitness_tracker = FitnessTracker()

        def test_set_and_view_profile(self):
            user_profile = UserProfile("John French", 180, "lbs")

            self.fitness_tracker.set_profile(user_profile)
            self.fitness_tracker.view_profile()

            assert self.fitness_tracker.profile.user_name == "John French"
            assert self.fitness_tracker.profile.user_weight == 180
            assert self.fitness_tracker.profile.weight_unit == "lbs"

        def test_clear_profile(self):
            user_profile = UserProfile("John French", 180, "lbs")

            self.fitness_tracker.set_profile(user_profile)
            self.fitness_tracker.clear_profile()

            assert self.fitness_tracker.profile is None

    # Workout tests
        def test_add_and_view_workouts(self):
            workout1 = Workout("Running", 30, 5, 300, "Morning run")
            workout2 = Workout("Cycling", 45, 4, 400, "Evening ride")

            self.fitness_tracker.add_workout(workout1)
            self.fitness_tracker.add_workout(workout2)
            self.fitness_tracker.view_workouts()

            assert len(self.fitness_tracker.workouts) == 2

        def test_workout_summary(self):
            workout1 = Workout("Running", 30, 5, 300, "Morning run")
            workout2 = Workout("Cycling", 45, 4, 400, "Evening ride")

            self.fitness_tracker.add_workout(workout1)
            self.fitness_tracker.add_workout(workout2)
            self.fitness_tracker.view_workouts()

            self.fitness_tracker.workout_summary()

            assert self.fitness_tracker.workouts[0].workout_duration + self.fitness_tracker.workouts[1].workout_duration == 75

        def test_clear_workouts(self):
            workout1 = Workout("Running", 30, 5, 300, "Morning run")
            workout2 = Workout("Cycling", 45, 4, 400, "Evening ride")

            self.fitness_tracker.add_workout(workout1)
            self.fitness_tracker.add_workout(workout2)
            self.fitness_tracker.clear_workouts()

            assert len(self.fitness_tracker.workouts) == 0

    # Goal tests
        def test_add_and_view_goals(self):
            goal1 = Goal(3, 150, 2000, "Swimming")
            goal2 = Goal(4, 200, 2500, "Running")

            self.fitness_tracker.add_goal(goal1)
            self.fitness_tracker.add_goal(goal2)
            self.fitness_tracker.view_goals()

            assert len(self.fitness_tracker.goals) == 2

if __name__ == '__main__':
    unittest.main()