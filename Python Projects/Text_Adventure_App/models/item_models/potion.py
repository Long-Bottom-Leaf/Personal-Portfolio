# Potion Child Class

from item_models.item import Item

class Potion(Item):
    def __init__(self, name, restoration_type, gold_value=0):
        super().__init__(name, gold_value)

        self.restoration_type = restoration_type