from Objects.Inventory import Inventory


class Character:
    """
    Base character class to be inherited by monsters, the player, and NPCs
    """
    def __init__(self):
        self.inventory = Inventory()
