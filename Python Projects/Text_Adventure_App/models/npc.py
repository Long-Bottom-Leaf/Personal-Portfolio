# NPC Parent

from models.character import Character

class Player_Character(Character):

    def __initi__(self, name, race, current_health, max_health, luck, armor=None, weapon=None, gold=0):

        super().__init__(
            name, race, current_health, max_health, armor, weapon
        )