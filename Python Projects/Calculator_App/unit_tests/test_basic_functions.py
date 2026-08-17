import sys
import os
import unittest

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from functions.math_functions import (
    add,
    subtract,
    multiply,
    divide
)

class TestBasicFunctions(unittest.TestCase):

    # Test basic functions
    def test_addition(self):
        self.assertEqual(add(2, 3), 5)

    def test_subtraction(self):
        self.assertEqual(subtract(5, 3), 2)

    def test_multiplication(self):
        self.assertEqual(multiply(5, 5), 25)

    def test_division(self):
        self.assertEqual(divide(5, 5), 1)

    def test_addition_multiple_numbers(self):
        self.assertEqual(add(1, 2, 3, 4, 5), 15)

    # Test multiple numbers
    def test_subtraction_multiple_numbers(self):
        self.assertEqual(subtract(20, 5, 3, 2), 10)


    def test_multiplication_multiple_numbers(self):
        self.assertEqual(multiply(2, 3, 4), 24)


    def test_division_multiple_numbers(self):
        self.assertEqual(divide(100, 2, 5), 10)

if __name__ == "__main__":
    unittest.main()