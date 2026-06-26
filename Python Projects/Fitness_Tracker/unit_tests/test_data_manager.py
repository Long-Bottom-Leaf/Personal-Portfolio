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

if __name__ == '__main__':
    unittest.main()