# Item Parent Test

import sys
import os
import unittest

project_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(project_root)

from models.item_models.item import Item

class TestItem(unittest.TestCase):

    def test_item_init(self):
        item = Item(
            name="Iron Sword",
            gold_value=5,
            is_equipped=False
        )

        self.assertEqual(item.name, "Iron Sword")
        self.assertEqual(item.gold_value, 5)
        self.assertEqual(item.is_equipped, False)

    def test_item_equipped(self):
        item = Item(
            name="Battle Axe",
            gold_value=6,
            is_equipped=True
        )
        
        self.assertEqual(item.name, "Battle Axe")
        self.assertEqual(item.gold_value, 6)
        self.assertEqual(item.is_equipped, True)

if __name__ == '__main__':
    unittest.main()