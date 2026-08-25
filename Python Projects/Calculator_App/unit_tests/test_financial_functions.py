import sys
import os
import unittest

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from functions.math_functions import (
    simple_interest,
)

class TestFinancialFunctions(unittest.TestCase):

    def test_simple_interest(self):
        self.assertEqual(simple_interest(1000, 5, 2), 100)

    def test_simple_interest_zero_rate(self):
        self.assertEqual(simple_interest(1000, 0, 5), 0)

    def test_simple_interest_zero_time(self):
        self.assertEqual(simple_interest(1000, 5, 0), 0)

    def test_compound_interest(self):
        self.assertEqual

if __name__ == "__main__":
    unittest.main()