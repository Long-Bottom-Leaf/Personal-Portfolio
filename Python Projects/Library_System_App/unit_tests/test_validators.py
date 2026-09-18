# Validator tests

import sys
import os
import unittest

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils.validators import (
    validate_non_empty,
    validate_release_date,
    validate_rating
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

if __name__ == "__main__":
    unittest.main()