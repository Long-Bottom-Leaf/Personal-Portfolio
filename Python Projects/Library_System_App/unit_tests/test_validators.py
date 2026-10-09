# Validator tests

import sys
import os
import unittest

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils.validators import (
    validate_non_empty,
    validate_release_date,
    validate_rating,
    validate_status,
    validate_menu_choice
)

class TestValidators(unittest.TestCase):

    def test_non_empty_string(self):
        self.assertEqual(validate_non_empty("Hello"), True)
        self.assertEqual(validate_non_empty("  World  "), True)
        self.assertEqual(validate_non_empty(""), False)
        self.assertEqual(validate_non_empty("   "), False)

    def test_empty_string(self):
        self.assertEqual(validate_non_empty(""), False)
        self.assertEqual(validate_non_empty("   "), False)

    def test_validate_release_date(self):
        self.assertEqual(validate_release_date("2026-01-01"), True)
        self.assertEqual(validate_release_date("2026-12-31"), True)
        self.assertEqual(validate_release_date(""), True)  # Empty string is valid
        self.assertEqual(validate_release_date("2026-01-35"), False)
        self.assertEqual(validate_release_date("2026-13-01"), False)
        self.assertEqual(validate_release_date("12-01-2026"), False)

    def test_validate_rating(self):
        self.assertEqual(validate_rating(""), True)
        self.assertEqual(validate_rating("0"), True)
        self.assertEqual(validate_rating("2.5"), True)
        self.assertEqual(validate_rating("5"), True)
        self.assertEqual(validate_rating("-2"), False)
        self.assertEqual(validate_rating("66"), False)
        self.assertEqual(validate_rating("Hello"), False)

    def test_validate_menu_choice(self):
        valid_choices = ["1", "2", "3"]

        self.assertTrue(validate_menu_choice("1", valid_choices))
        self.assertTrue(validate_menu_choice("2", valid_choices))
        self.assertFalse(validate_menu_choice("4", valid_choices))
        self.assertFalse(validate_menu_choice("", valid_choices))

    def test_validate_status(self):
        self.assertTrue(validate_status("Y"))
        self.assertTrue(validate_status("N"))
        self.assertFalse(validate_status("X"))
        self.assertFalse(validate_status(""))

if __name__ == "__main__":
    unittest.main()