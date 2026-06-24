# Test fitness tracker service

import sys
import os
import unittest

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from services.fitness_tracker import FitnessTrackerService

class TestFitnessTracker(unittest.TestCase):

    def setUp(self):
        self.fitness_tracker = FitnessTrackerService()