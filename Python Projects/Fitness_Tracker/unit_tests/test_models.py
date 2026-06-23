# Test program models
import sys
import os
import unittest

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from models.user_profile import UserProfile

# User Profile
class TestUserProfile(unittest.TestCase):

    def test_user_profile_creation(self):
        user_profile = UserProfile("John French", 180, "lbs")

        self.assertEqual(user_profile.user_name, "John French")
        self.assertEqual(user_profile.user_weight, 180)
        self.assertEqual(user_profile.weight_unit, 'lbs')

# Workout


# Goal


if __name__ == '__main__':
    unittest.main()