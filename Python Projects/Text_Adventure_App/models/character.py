# Character
class Character:

    def __init__(self, name, race, current_health, max_health, armor=None, weapon=None):
        self.name = name
        self.race = race
        self.current_health = current_health
        self.max_health = max_health
        self.armor = armor
        self.weapon = weapon

    def __str__(self):
        return (
            f"Name: {self.name}\n"
            f"Race: {self.race}\n"
            f"Health: {self.current_health}\n"
            f"Max Health: {self.max_health}\n"
            f"Armor: {self.armor}\n"
            f"Weapon: {self.weapon}\n"
        )