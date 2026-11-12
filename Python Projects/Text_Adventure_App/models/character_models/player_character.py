# Player Character
from models.character_models.character import Character

class Player_Character(Character):

    def __initi__(self, name, race, current_health, max_health, luck, inventory, armor=None, weapon=None, gold=0):

        super().__init__(
            name, race, current_health, max_health, armor, weapon
        )

        self.luck = luck
        self.inventory = inventory
        self.gold = gold