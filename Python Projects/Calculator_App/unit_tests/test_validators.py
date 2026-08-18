import sys
import os
import unittest

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils.validators import (
    validate_menu_choice,
    validate_number
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

if __name__ == "__main__":
    unittest.main()