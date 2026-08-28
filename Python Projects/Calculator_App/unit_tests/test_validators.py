import sys
import os
import unittest
from unittest.mock import patch

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils.validators import (
    validate_menu_choice,
    validate_number,
    validate_minimum_numbers,
    get_valid_number,
    validate_positive_number
)

class TestValidators(unittest.TestCase):

    def test_validate_menu_choice(self):

        choices = ["1", "2", "3"]

        self.assertTrue(validate_menu_choice("1", choices))
        self.assertTrue(validate_menu_choice("2", choices))
        self.assertFalse(validate_menu_choice("6", choices))

    def test_validate_number(self):

        self.assertTrue(validate_number("10"))
        self.assertTrue(validate_number("5.5"))
        self.assertTrue(validate_number("-10"))
        self.assertTrue(validate_number("0"))
        self.assertFalse(validate_number("Hello world!"))

    def test_validate_minimum_numbers(self):

        self.assertTrue(validate_minimum_numbers([1, 2], 2))
        self.assertTrue(validate_minimum_numbers([1, 2, 3], 2))
        self.assertFalse(validate_minimum_numbers([1], 2))

    def test_validate_positive_number(self):

        self.assertTrue(validate_positive_number(10))
        self.assertTrue(validate_positive_number(0.5))
        self.assertFalse(validate_positive_number(0))
        self.assertFalse(validate_positive_number(-10))

    def test_get_valid_number(self):

        with patch("builtins.input", return_value="25"):
            result = get_valid_number("Enter number: ")

        self.assertEqual(result, 25.0)

    def test_get_valid_number_invalid_then_valid(self):

        with patch("builtins.input", side_effect=["hello", "25"]):
            result = get_valid_number("Enter number: ")

        self.assertEqual(result, 25.0)

if __name__ == "__main__":
    unittest.main()