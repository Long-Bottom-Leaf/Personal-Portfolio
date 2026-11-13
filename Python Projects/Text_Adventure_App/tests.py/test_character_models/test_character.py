# Character Parent Test

import sys
import os
import unittest

project_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(project_root)

from models.character_models.character import Character

class TestCharacter(unittest.TestCase):

    def test_character_init(self):
        character = Character(
            name="Bilbo",
            race="Hobbit",
            current_health=15,
            max_health=20,
            armor=None,
            weapon=None
        )

        self.assertEqual(character.name, "Bilbo")
        self.assertEqual(character.race, "Hobbit")
        self.assertEqual(character.current_health, 15)
        self.assertEqual(character.max_health, 20)
        self.assertIsNone(character.armor)
        self.assertIsNone(character.weapon)

    def test_character_with_equippment(self):
        character = Character(
            name="Bilbo",
            race="Hobbit",
            current_health=15,
            max_health=20,
            armor="Leather Armor",
            weapon="Iron Sword"
        )

        self.assertEqual(character.armor, "Leather Armor")
        self.assertEqual(character.weapon, "Iron Sword")

    def test_character_str(self):
        character = Character("Bilbo", "Hobbit", 15, 20)

        expected = (
            "Name: Bilbo\n"
            "Race: Hobbit\n"
            "Health: 15\n"
            "Max Health: 20\n"
            "Armor: None\n"
            "Weapon: None\n"
        )

        self.assertEqual(str(character), expected)

if __name__ == '__main__':
    unittest.main()