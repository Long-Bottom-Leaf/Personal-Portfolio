# Shopkeeper Child Test

import sys
import os
import unittest

project_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(project_root)

from models.character_models.shop_keeper import ShopKeeper

class TestShopkeer (unittest.TestCase):

    def test_shopkeeper_init(self):
        character = ShopKeeper(
            name="Timmy",
            race="Gnome",
            current_health=15,
            max_health=20,
            dialogue="Welcome to my shop!",
            disposition="Friendly",
            npc_identifier=2,
            inventory=None,
            armor=None,
            weapon=None
        )

        # Inherited Character attributes
        self.assertEqual(character.name, "Timmy")
        self.assertEqual(character.race, "Gnome")
        self.assertEqual(character.current_health, 15)
        self.assertEqual(character.max_health, 20)
        self.assertIsNone(character.armor)
        self.assertIsNone(character.weapon)

        # Inherited NPC attributes
        self.assertEqual(character.dialogue, "Welcome to my shop!")
        self.assertEqual(character.disposition, "Friendly")
        self.assertEqual(character.npc_identifier, 2)

        # ShopKeeper attributes
        self.assertEqual(character.inventory, [])


if __name__ == '__main__':
    unittest.main()

        