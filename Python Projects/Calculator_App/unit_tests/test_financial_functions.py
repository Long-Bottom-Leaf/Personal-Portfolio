import sys
import os
import unittest

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from functions.math_functions import (
    simple_interest,
    compound_interest
)

class TestFinancialFunctions(unittest.TestCase):

    # Simple Interest
    def test_simple_interest(self):
        self.assertEqual(simple_interest(1000, 5, 2), 100)

    def test_simple_interest_zero_rate(self):
        self.assertEqual(simple_interest(1000, 0, 5), 0)

    def test_simple_interest_zero_time(self):
        self.assertEqual(simple_interest(1000, 5, 0), 0)

    # Compound Interest
    def test_compound_interest(self):
        result = compound_interest(10000.0, 5.0, 1, 10.0)
        self.assertAlmostEqual(result, 16288.95, places=2)


    def test_monthly_compound(self):
        result = compound_interest(1000.0, 5.0, 12, 10.0)
        self.assertAlmostEqual(result, 1647.01, places=2)


    def test_zero_interest_rate(self):
        result = compound_interest(1000.0, 0.0, 12, 5.0)
        self.assertAlmostEqual(result, 1000.0, places=2)


    def test_compound_interest_zero_time(self):
        result = compound_interest(1000.0, 5.0, 12, 0.0)
        self.assertAlmostEqual(result, 1000.0, places=2)

if __name__ == "__main__":
    unittest.main()