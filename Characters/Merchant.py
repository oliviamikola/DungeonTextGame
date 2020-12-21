from Characters.Character import Character
from Objects.Item import Item


class Merchant(Character):
    """
    Class representation of the merchant
    """

    def __init__(self):
        Character.__init__(self)

    def DisplayWares(self):
        """
        Displays what is in the merchant's inventory
        :return: None
        """
        print("{:<20s}{}".format("Item", "Cost"))
        for item in self.inventory.inventory:
            print("{:<15s}{}".format(item.name, item.price))

    def SellWare(self, itemName: str) -> Item:
        """
        Sells a ware to a player
        :param itemName: desired item to sell
        :return: True if merchant sells that item, False otherwise
        """
        return self.inventory[itemName]
