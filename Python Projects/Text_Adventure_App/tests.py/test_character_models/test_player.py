# Player Child Test

import sys
import os
import unittest

project_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(project_root)

from models.character_models.player_character import PlayerCharacter

class TestPlayer(unittest.TestCase):

    def test_player_character(self):
        player_character = PlayerCharacter(
            name="Bilbo",
            race="Hobbit",
            current_health=15,
            max_health=20,
            luck=15,
            inventory=[],
            armor=None,
            weapon=None,
            gold=20
        )

        # Inherited attributes
        self.assertEqual(player_character.name, "Bilbo")
        self.assertEqual(player_character.race, "Hobbit")
        self.assertEqual(player_character.current_health, 15)
        self.assertEqual(player_character.max_health, 20)

        # Player-specific attributes
        self.assertEqual(player_character.luck, 15)
        self.assertEqual(player_character.inventory, [])
        self.assertEqual(player_character.gold, 20)

    def test_player_default_inventory(self):
        player_character = PlayerCharacter(
            name="Bilbo",
            race="Hobbit",
            current_health=15,
            max_health=20,
            luck=15
        )

        self.assertEqual(player_character.inventory, [])

    def test_player_inventory_independence(self):
        player1 = PlayerCharacter("Bilbo", "Hobbit", 15, 20, 15)
        player2 = PlayerCharacter("Frodo", "Hobbit", 15, 20, 15)

        player1.inventory.append("Iron Sword")

        self.assertEqual(player1.inventory, ["Iron Sword"])
        self.assertEqual(player2.inventory, [])

if __name__ == '__main__':
    unittest.main()