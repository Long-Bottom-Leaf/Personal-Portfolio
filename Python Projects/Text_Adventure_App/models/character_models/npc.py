# NPC Parent
from models.character_models.character import Character

class NPC(Character):
    def __init__(self, name, race, current_health, max_health, dialogue, disposition, npc_identifier, armor=None, weapon=None):

        super().__init__(
            name, race, current_health, max_health, armor, weapon
        )

        self.dialogue = dialogue
        self.disposition = disposition
        self.npc_identifier = npc_identifier