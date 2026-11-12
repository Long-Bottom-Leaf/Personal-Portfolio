# Item Parent Class

class Item:
    def __init__(self, name, gold_value=0, is_equipped=False):
        self.name = name
        self.gold_value = gold_value
        self.is_equipped = is_equipped

    def __str__(self):
        return (
            f"Name: {self.name}\n"
            f"Gold Value: {self.gold_value}\n"
        )