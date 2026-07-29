# Store data as JSON file, can update to SQL later

import json
import os

from utils.error_messages import (
    FILE_LOAD_ERROR,
    FILE_SAVE_ERROR
)
from utils.success_messages import (
    FILE_LOAD,
    FILE_SAVED
)

class DataManager:

    def __init__(self, file_path = "data/fitness_data.json"):
        self.file_path = file_path

    def create_file_if_missing(self):
        os.makedirs(os.path.dirname(self.file_path), exist_ok=True)

        if not os.path.isfile(self.file_path):
            starter_data = {
                "profile": None,
                "workouts": [],
                "goals": []
            }

            with open(self.file_path, "w") as file:
                json.dump(starter_data, file, indent = 4)

    def load_data(self):
        self.create_file_if_missing()

        try:
            with open(self.file_path, 'r') as file:
                data = json.load(file)
            
                print(FILE_LOAD)
                return data
        
        except (OSError, json.JSONDecodeError):
            print(FILE_LOAD_ERROR)
            return data

    def save_data(self, data):
        self.create_file_if_missing()

        try:
            with open(self.file_path, 'w') as file:
                json.dump(data, file, indent = 4)
            
                print(FILE_SAVED)
                
        except OSError:
            print(FILE_SAVE_ERROR)