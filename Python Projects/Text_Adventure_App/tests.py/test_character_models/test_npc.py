# NPC Child Test

import sys
import os
import unittest

project_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(project_root)

from models.character_models.npc import NPC

class TestNPC(unittest.TestCase):

    def test_npc_init(self):
        character = NPC(
            name="Bilbo",
            race="Hobbit",
            current_health=15,
            max_health=20,
            dialogue="Hello Adventurer!",
            disposition="Friendly",
            npc_identifier=1,
            armor=None,
            weapon=None
        )

        self.assertEqual(character.name, "Bilbo")
        self.assertEqual(character.race, "Hobbit")
        self.assertEqual(character.current_health, 15)
        self.assertEqual(character.max_health, 20)
        self.assertEqual(character.dialogue, "Hello Adventurer!")
        self.assertEqual(character.disposition, "Friendly")
        self.assertEqual(character.npc_identifier, 1)
        self.assertIsNone(character.armor)
        self.assertIsNone(character.weapon)

    def test_npc_equipment(self):
        character = NPC(
            name="Guard",
            race="Human",
            current_health=20,
            max_health=20,
            dialogue="Halt!",
            disposition="Hostile",
            npc_identifier=2,
            armor="Chainmail",
            weapon="Iron Sword"
        )

        self.assertEqual(character.armor, "Chainmail")
        self.assertEqual(character.weapon, "Iron Sword")

if __name__ == '__main__':
    unittest.main()