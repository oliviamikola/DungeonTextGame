from typing import Tuple
from Characters.AttackingCharacter import AttackingCharacter
from Characters.Merchant import Merchant
from Objects.MoneyAmount import MoneyAmount
from MapObjects.Room import Room


class Player(AttackingCharacter):
    """
    Class representing the player who is playing the game
    """

    def __init__(self):
        AttackingCharacter.__init__(self)
        self.health.SetNewMax(100)
        self.health.SetToMax()
        self.purse = MoneyAmount()
        self.currentRoom: Room = None

    def __repr__(self):
        return f"Health: {self.health}\nInventory: {self.inventory}"

    def _ResetStats(self):
        self.health.SetToMax()

    def Attack(self):
        pass

    def Purchase(self, merchant: Merchant, itemName: str, amount: int = 1) -> Tuple[bool, str]:
        """
        Purchases an item from a merchant
        :param merchant: the merchant who the player is buying an item from
        :param itemName: name of the item player wants to purchase
        :param amount: how many times the player wants to buy itemName
        :return: bool of whether purchase was successful and a message for why the purchase was not successful if failed
        """
        item = merchant.SellWare(itemName)
        if item is None:
            return False, f"Merchant does not carry {itemName}"
        if (item.price * amount) > self.purse:
            return False, f"Player does not have enough money to pay for {amount}x{itemName} each costing {item.price}"
        if not self.inventory.Add(item):
            return False, f"Not enough room in inventory for {itemName}"
        self.purse.Subtract(item.price)
        return True, f"Successfully bought {itemName}"

    def Sell(self, itemName: str, amount: int = 1) -> Tuple[bool, str]:
        """
        Sells an item
        :param itemName: name of item to sell
        :return: True if item was sold, False otherwise
        """
        item = self.inventory[itemName]
        if item is None:
            return False, f"Player does not have {itemName} in their inventory"
        amountInInventory = self.inventory.GetAmountOfItem(item)
        if amountInInventory < amount:
            return False, f"Player does not have {amount}x{itemName} in their inventory"
        for _ in range(amount):
            self.inventory.Remove(item)
            self.purse.Add(item.price)
        return True, f"Successfully sold {itemName}"
