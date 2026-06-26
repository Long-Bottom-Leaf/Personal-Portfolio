# Test data manager service

import sys
import os
import unittest
import tempfile

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from storage.data_manager import DataManager

class TestDataManager(unittest.TestCase):

    def test_create_file_if_missing(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            test_file_path = os.path.join(temp_dir, "fitness_data.json")

            data_manager = DataManager(test_file_path)
            data_manager.create_file_if_missing()

            self.assertTrue(os.path.isfile(test_file_path))

    def test_load_data_has_start_data(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            test_file_path = os.path.join(temp_dir, "fitness_data.json")

            data_manager = DataManager(test_file_path)
            data = data_manager.load_data()

            self.assertEqual(data["profile"], None)
            self.assertEqual(data["workouts"], [])
            self.assertEqual(data["goals"], [])

    def test_save_data(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            test_file_path = os.path.join(temp_dir, "fitness_data.json")

            data_manager = DataManager(test_file_path)

            test_data = {
                "profile": {
                    "name": "Stephen",
                    "weight": 180,
                    "weight_unit": "lbs"
                },
                "workouts": [],
                "goals": []
            }

            data_manager.save_data(test_data)
            loaded_data = data_manager.load_data()

            self.assertEqual(loaded_data, test_data)

if __name__ == '__main__':
    unittest.main()