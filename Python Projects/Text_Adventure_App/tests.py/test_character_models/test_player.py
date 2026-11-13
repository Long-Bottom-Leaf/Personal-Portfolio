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

if __name__ == '__main__':
    unittest.main()