class Item:
    """
    Base class for all items possibly stored in an inventory
        i.e. armor, weapons, potions, etc.
    """
    def __init__(self):
        self.isStackable = True
