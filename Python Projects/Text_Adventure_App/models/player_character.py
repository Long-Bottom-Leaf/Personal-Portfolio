# Player Character Class

class Player_Character:

    def __init__(self, name, health, armor, weapon, luck, gold, misc_inventory, loot):
        self.name = name
        self.health = health
        self.armor = armor
        self.weapon = weapon
        self.luck = luck
        self.gold = gold
        self.misc_inventory = misc_inventory
        self.loot = loot

    def __str__(self):
        f"Name: {self.name}\n"
        f"Health: {self.health}\n"
        f"Armor: {self.armor}\n"
        f"Weapon: {self.weapon}\n"
        f"Luck: {self.luck}\n"
        f"Gold: {self.gold}\n"
        f"Misc Items: {self.misc_inventory}\n"
        f"Valuables: {self.loot}\n"