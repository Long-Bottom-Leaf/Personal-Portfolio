# Weapon Child Test

import sys
import os
import unittest

project_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(project_root)

from models.item_models.weapon import Weapon

class TestWeapon(unittest.TestCase):

    def test_weapon_init(self):
        weapon = Weapon(
            name="Balanced Sword",
            success_bonus=1,
            damage_bonus=1,
            gold_value=5,
            is_equipped=False
        )

        # Inherited Attributes
        self.assertEqual(weapon.name, "Balanced Sword")
        self.assertEqual(weapon.gold_value, 5)
        self.assertEqual(weapon.is_equipped, False)

        # Weapon Attributes
        self.assertEqual(weapon.success_bonus, 1)
        self.assertEqual(weapon.damage_bonus, 1)

if __name__ == '__main__':
    unittest.main()