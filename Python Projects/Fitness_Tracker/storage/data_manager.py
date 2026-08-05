# Store data as JSON file, can update to SQL later

import json
import os
from datetime import date

from models.user_profile import UserProfile
from models.workout import Workout
from models.goal import Goal

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
            return None

# save data
    def save_data(self, data):
        self.create_file_if_missing()

        try:
            with open(self.file_path, 'w') as file:
                json.dump(data, file, indent = 4)
            
                print(FILE_SAVED)
                
        except OSError:
            print(FILE_SAVE_ERROR)

# convert objects to json
    def save_tracker(self, fitness_tracker):
        data = {
            "profile": None,
            "workouts": [],
            "goals": []
        }

        if fitness_tracker.profile:
            data["profile"] = {
                "name": fitness_tracker.profile.user_name,
                "weight": fitness_tracker.profile.user_weight,
                "weight_unit": fitness_tracker.profile.weight_unit
            }

        for workout in fitness_tracker.workouts:
            data["workouts"].append({
                "date": str(workout.workout_date),
                "type": workout.workout_type,
                "duration": workout.workout_duration,
                "intensity": workout.workout_intensity,
                "calories": workout.calories_burned,
                "notes": workout.notes
            })

        for goal in fitness_tracker.goals:
            data["goals"].append({
                "count": goal.weekly_workout_count,
                "duration": goal.weekly_duration,
                "calories": goal.weekly_calories,
                "type": goal.workout_type_goal
            })

        self.save_data(data)

    def load_tracker(self, fitness_tracker):
        data = self.load_data()

        if data is None:
            return

        # Profile
        fitness_tracker.profile = None

        profile_data = data.get("profile")

        if profile_data:
            fitness_tracker.profile = UserProfile(
                profile_data["name"],
                profile_data["weight"],
                profile_data["weight_unit"]
            )

        # Workouts
        fitness_tracker.workouts.clear()

        for workout_data in data.get("workouts", []):
            workout = Workout(
                workout_data["type"],
                workout_data["duration"],
                workout_data["intensity"],
                workout_data["calories"],
                workout_data["notes"]
            )

            workout.workout_date = date.fromisoformat(
                workout_data["date"]
            )

            fitness_tracker.workouts.append(workout)

        # Goals
        fitness_tracker.goals.clear()

        for goal_data in data.get("goals", []):
            goal = Goal(
                goal_data["count"],
                goal_data["duration"],
                goal_data["calories"],
                goal_data["type"]
            )

            fitness_tracker.goals.append(goal)