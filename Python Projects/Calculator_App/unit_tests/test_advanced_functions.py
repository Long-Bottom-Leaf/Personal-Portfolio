import sys
import os
import unittest

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from functions.math_functions import (
    square_root,
    power,
    percent,
    absolute_value
)

class TestAdvancedFunctions(unittest.TestCase):

    def test_square_root(self):
        self.assertEqual(square_root(25), 5)

    def test_square_root_negative(self):
        with self.assertRaises(ValueError):
            square_root(-25)

    def test_power(self):
        self.assertEqual(power(2, 3), 8)

    def test_percentage(self):
        self.assertEqual(percent(200, 15), 30)

    def test_absolute_value(self):
        self.assertEqual(absolute_value(-25), 25)

if __name__ == "__main__":
    unittest.main()