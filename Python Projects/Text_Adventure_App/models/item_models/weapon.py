# Weapon Child Class

from item_models.item import Item

class Weapon(Item):
    def __init__(self, name, success_bonus=0, damage_bonus=0, gold_value=0, *, is_equipped=False):
        super().__init__(
            name, gold_value, is_equipped
        )

        self.success_bonus = success_bonus
        self.damage_bonus = damage_bonus