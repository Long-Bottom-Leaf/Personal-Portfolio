# Enemy Combatant
from models.character_models.npc import NPC

class Enemy(NPC):
    def __init__(self, name, race, current_health, max_health, dialogue, disposition, npc_identifier, loot_drop, armor=None, weapon=None,):
    
        super().__init__(
            name, race, current_health, max_health, dialogue, disposition, npc_identifier, armor, weapon
        )
    
        self.loot_drop = loot_drop