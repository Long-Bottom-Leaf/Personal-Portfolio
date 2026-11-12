# Shop NPC
from models.character_models.character import Character

class Shop_Keeper(Character):
    def __initi__(self, name, race, current_health, max_health, inventory, armor=None, weapon=None):
    
        super().__init__(
            name, race, current_health, max_health, armor, weapon
        )
    
        self.inventory = inventory