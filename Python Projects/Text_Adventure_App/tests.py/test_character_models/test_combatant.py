# Combatant Child Test

import sys
import os
import unittest

project_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(project_root)

from models.character_models.combatant import Enemy

class TestCombatant(unittest.TestCase):

    def test_combatant_init(self):
        character = Enemy(
            name="Gorbo",
            race="Goblin",
            current_health=15,
            max_health=20,
            dialogue="Time to fight!",
            disposition="Hostile",
            npc_identifier=1,
            loot_drop=["Gold", "Health Potion"],
            armor=None,
            weapon=None
        )

        # Character attributes
        self.assertEqual(character.name, "Gorbo")
        self.assertEqual(character.race, "Goblin")
        self.assertEqual(character.current_health, 15)
        self.assertEqual(character.max_health, 20)

        # NPC attributes
        self.assertEqual(character.dialogue, "Time to fight!")
        self.assertEqual(character.disposition, "Hostile")
        self.assertEqual(character.npc_identifier, 1)

        # Enemy attributes
        self.assertEqual(character.loot_drop, ["Gold", "Health Potion"])

        # Equipment
        self.assertIsNone(character.armor)
        self.assertIsNone(character.weapon)

if __name__ == '__main__':
    unittest.main()