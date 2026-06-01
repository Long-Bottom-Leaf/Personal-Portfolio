# User Profile model

from datetime import date

class UserProfile:

    def __init__(self, name, weight, weight_unit):

        self.user_name = name
        self.user_weight = weight
        self.weight_unit = weight_unit
        self.profile_creation = date.today()

    def __str__(self):

        return f"Name: {self.user_name}, Weight: {self.user_weight} {self.weight_unit}, Profile created on: {self.profile_creation}"