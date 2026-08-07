import sys
import os
import unittest
from datetime import date

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils.formatters import FormatDate1, FormatDate2, FormatDate3
from utils.validators import (
    validate_positive_number,
    validate_goal_count,
    validate_weight_unit,
    validate_intensity,
    validate_activity,
    validate_menu_choice,
    validate_date,
    validate_name
)
from utils.error_messages import (
    NO_PROFILE,
    INVALID_WEIGHT,
    INVALID_GOAL_COUNT,
    FILE_SAVE_ERROR,
    INVALID_MENU_CHOICE
)


class TestDateFormatters(unittest.TestCase):

    def test_format_date_1(self):
        test_date = date(2026, 6, 23)

        self.assertEqual(FormatDate1(test_date), "2026-06-23")

    def test_format_date_2(self):
        test_date = date(2026, 6, 23)

        self.assertEqual(FormatDate2(test_date), "23-Jun-26")

    def test_format_date_3(self):
        test_date = date(2026, 6, 23)

        self.assertEqual(FormatDate3(test_date), "Tuesday, June 23, 2026")


class TestValidators(unittest.TestCase):

    def test_validate_positive_number(self):
        self.assertTrue(validate_positive_number("10"))
        self.assertFalse(validate_positive_number("0"))
        self.assertFalse(validate_positive_number("-5"))
        self.assertFalse(validate_positive_number("abc"))

    def test_validate_name(self):
        self.assertTrue(validate_name("Stephen"))
        self.assertTrue(validate_name("Mary Jane"))
        self.assertTrue(validate_name("Anne-Marie"))
        self.assertTrue(validate_name("O'Connor"))

        self.assertFalse(validate_name(""))
        self.assertFalse(validate_name("A"))
        self.assertFalse(validate_name("Jo"))
        self.assertFalse(validate_name("123"))
        self.assertFalse(validate_name("@Stephen"))

    def test_validate_goal_count(self):
        self.assertTrue(validate_goal_count("0"))
        self.assertTrue(validate_goal_count("3"))
        self.assertFalse(validate_goal_count("-1"))
        self.assertFalse(validate_goal_count("abc"))

    def test_validate_weight_unit(self):
        self.assertTrue(validate_weight_unit("lbs"))
        self.assertTrue(validate_weight_unit("kgs"))
        self.assertTrue(validate_weight_unit(" LBS "))
        self.assertFalse(validate_weight_unit("stones"))

    def test_validate_intensity(self):
        self.assertTrue(validate_intensity("low"))
        self.assertTrue(validate_intensity("Medium"))
        self.assertTrue(validate_intensity(" HIGH "))
        self.assertFalse(validate_intensity("extreme"))

    def test_validate_activity(self):
        self.assertTrue(validate_activity("R"))
        self.assertTrue(validate_activity("r"))
        self.assertFalse(validate_activity("X"))

    def test_validate_menu_choice(self):
        valid_choices = ["1", "2", "3"]

        self.assertTrue(validate_menu_choice("1", valid_choices))
        self.assertTrue(validate_menu_choice(" 2 ", valid_choices))
        self.assertFalse(validate_menu_choice("5", valid_choices))

    def test_validate_date(self):
        self.assertTrue(validate_date("2026-06-23"))
        self.assertFalse(validate_date("06-23-2026"))
        self.assertFalse(validate_date("not a date"))


class TestErrorMessages(unittest.TestCase):

    def test_no_profile_message(self):
        self.assertEqual(
            NO_PROFILE,
            "Error: No profile found. Please create a profile first."
        )

    def test_invalid_weight_message(self):
        self.assertEqual(
            INVALID_WEIGHT,
            "Error: Invalid weight. Weight must be greater than 0."
        )

    def test_invalid_goal_count_message(self):
        self.assertEqual(
            INVALID_GOAL_COUNT,
            "Error: Invalid number. Please enter 0 or greater."
        )

    def test_file_save_error_message(self):
        self.assertEqual(
            FILE_SAVE_ERROR,
            "Error: Unable to save data."
        )

    def test_invalid_menu_choice_message(self):
        self.assertEqual(
            INVALID_MENU_CHOICE,
            "Error: Invalid menu choice. Please select a valid option."
        )


if __name__ == "__main__":
    unittest.main()