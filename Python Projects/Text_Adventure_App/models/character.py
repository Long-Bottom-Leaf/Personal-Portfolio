# Character
class Character:

    def __init__(self, name, race, current_health, max_health, armor=None, weapon=None, luck=0, gold=0, misc_inventory=None, loot=None):
        self.name = name
        self.race = race
        self.current_health = current_health
        self.max_health = max_health
        self.armor = armor
        self.weapon = weapon
        self.luck = luck
        self.gold = gold
        self.misc_inventory = misc_inventory
        self.loot = loot

    def __str__(self):
        f"Name: {self.name}\n"
        f"Race: {self.race}\n"
        f"Health: {self.current_health}\n"
        f"Max Health: {self.max_health}\n"
        f"Armor: {self.armor}\n"
        f"Weapon: {self.weapon}\n"
        f"Luck: {self.luck}\n"
        f"Gold: {self.gold}\n"
        f"Misc Items: {self.misc_inventory}\n"
        f"Valuables: {self.loot}\n"