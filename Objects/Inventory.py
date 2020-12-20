from typing import Dict
from Objects.Item import Item
from Helpers.MaxTracker import MaxTracker


class Inventory:
    """
    Stores all objects a character may have
    """

    def __init__(self, inventorySize=10):
        self.inventory: Dict[Item, int] = {}
        self.size = MaxTracker(inventorySize)

    def __repr__(self):
        if len(self.inventory) == 0:
            return "Empty"
        rep = ""
        for item, count in self.inventory.items():
            rep += f"{item}"
            if item.isStackable:
                rep += f"x{count}"
            else:
                rep += f", {item}" * (count - 1)
            rep += ', '
        return rep.strip(", ")

    def GetSize(self):
        """
        Gets the current size of the inventory
        :return: amount of items in the inventory
        """
        return self.size.adjustable

    def GetMaxSize(self):
        """
        Gets the max size of the inventory
        :return: max size of inventory
        """
        return self.size.max

    def IncreaseSize(self, toIncrease):
        """
        Increases the size of the inventory
        :param toIncrease: amount to increase by
        :return: None
        """
        self.size.SetNewMax(self.size.max + toIncrease)

    def Clear(self):
        """
        Clears the inventory
        :return: None
        """
        self.inventory: Dict[Item, int] = {}
        self.size.SetToZero()

    def Add(self, item: Item) -> bool:
        """
        Adds item to the inventory
        :param item: item to add to inventory
        :return: True if item is successfully added, False otherwise
        """
        if item.isStackable:
            # TODO: Implement max stack size
            if not self.size.AtMax():  # Not at max size, can still add new items to inventory
                if item not in self.inventory:
                    self.inventory[item] = 0
                    self.size.AdjustUp()
            else:  # At max size, can only place in inventory if item already exists in inventory
                if item in self.inventory:
                    self.inventory[item] += 1
                    return True
                return False

            self.inventory[item] += 1
            return True

        else:
            if not self.size.AtMax():  # Can place item in inventory
                if item not in self.inventory:
                    self.inventory[item] = 0
                self.inventory[item] += 1
                self.size.AdjustUp()
                return True
            else:  # Cannot place item in inventory
                return False

    def Remove(self, item: Item) -> bool:
        """
        Removes an item from the inventory
        :param item: item to remove
        :return: True if item is successfully removed, False otherwise
        """
        if item not in self.inventory:
            return False

        self.inventory[item] -= 1

        if not item.isStackable or not self.inventory[item]:
            self.size.AdjustDown()

        if not self.inventory[item]:
            self.inventory.pop(item)

        return True
