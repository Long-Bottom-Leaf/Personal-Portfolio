# Armor Child Class

from item_models.item import Item

class Armor(Item):
    def __init__(self, name, armor_value=0, gold_value=0, *, is_equipped=False):
        super().__init__(name, gold_value, is_equipped)

        self.armor_value = armor_value