from Objects.MoneyAmount import MoneyAmount


class Item:
    """
    Base class for all items possibly stored in an inventory
        i.e. armor, weapons, potions, etc.
    """
    def __init__(self, name: str = "Some Item"):
        self.name = name
        self.price = MoneyAmount()
        self.isStackable = True

    def __str__(self):
        return f"{self.name}"

    # def __eq__(self, other):
    #     return self.name == other.name and self.price == other.price and self.isStackable == other.isStackable
