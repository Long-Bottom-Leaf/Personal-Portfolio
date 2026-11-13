# Shop NPC
from models.character_models.npc import NPC

class ShopKeeper(NPC):
    def __init__(self, name, race, current_health, max_health, dialogue, disposition, npc_identifier, inventory=None, armor=None, weapon=None):
    
        super().__init__(
            name, race, current_health, max_health, dialogue, disposition, npc_identifier, armor, weapon
        )
    
        self.inventory = [] if inventory is None else inventory