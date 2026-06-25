# Test goal tracker service

import sys
import os
import unittest
from io import StringIO
from contextlib import redirect_stdout

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from models.workout import Workout
from models.goal import Goal
from services.goal_tracker import GoalTracker

class TestGoalTracker(unittest.TestCase):

    def test_no_goals(self):
        workouts = [
            Workout("Running", 30, "medium", 400, "Test run")
        ]

        goal = []

        goal_tracker = GoalTracker(workouts, goal)

        output = StringIO()

        with redirect_stdout(output):
            goal_tracker.show_goal_progress()

        self.assertIn("No goals set.", output.getvalue())

    def test_no_workouts(self):
        workouts = []

        goal = [
            Goal(4, 120, 1500, "Running")
        ]

        goal_tracker = GoalTracker(workouts, goal)

        output = StringIO()

        with redirect_stdout(output):
            goal_tracker.show_goal_progress()

        self.assertIn("No workouts logged.", output.getvalue())

    def test_goal_progress(self):
        workouts = [
            Workout("Running", 30, "medium", 400, "Test run"),
            Workout("Cycling", 45, "high", 612, "Test ride")
        ]

        goals = [
            Goal(4, 120, 1500, "Running")
        ]

        goal_tracker = GoalTracker(workouts, goals)

        output = StringIO()

        with redirect_stdout(output):
            goal_tracker.show_goal_progress()

        result = output.getvalue()

        self.assertIn("Goal Progress #1", result)
        self.assertIn("Workout Count: 2/4", result)
        self.assertIn("Duration: 75/120 minutes", result)
        self.assertIn("Calories Burned: 1012/1500 kcal", result)
        self.assertIn("Running Workouts: 1", result)

if __name__ == '__main__':
    unittest.main()