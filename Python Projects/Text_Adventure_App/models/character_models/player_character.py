# Player Character
from models.character_models.character import Character

class PlayerCharacter(Character):
    def __init__(self, name, race, current_health, max_health, luck, inventory=None, armor=None, weapon=None, gold=0):

        super().__init__(
            name, race, current_health, max_health, armor, weapon
        )

        self.luck = luck
        self.inventory = [] if inventory is None else inventory
        self.gold = gold