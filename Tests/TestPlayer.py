import unittest
from Characters.Player import Player
from Characters.Merchant import Merchant
from Objects.Item import Item


class TestPlayer(unittest.TestCase):
    def PopulateMerchantInventory(self, merchant: Merchant) -> None:
        fp = open("ItemsForTesting.csv", "r")
        fp.readline()  # header
        for line in fp:
            line = line.strip().split(",")
            item = Item(line[0])
            item.price.gold = int(line[1])
            item.price.silver = int(line[2])
            item.isStackable = False if line[3] == "N" else True
            merchant.inventory.inventory[item] = 1
        fp.close()

    def PopulatePlayerInventory(self, player: Player) -> None:
        fp = open("ItemsForTesting.csv", "r")
        fp.readline()  # header
        for line in fp:
            line = line.strip().split(",")
            item = Item(line[0])
            item.price.gold = int(line[1])
            item.price.silver = int(line[2])
            item.isStackable = False if line[3] == "N" else True
            player.inventory.Add(item)

        potion_item = player.inventory["Potion of Healing"]
        for _ in range(6):
            player.inventory.Add(potion_item)

        fp.close()

    def GivePlayerMoney(self, player: Player, gold: int, silver: int) -> None:
        player.purse.gold = gold
        player.purse.silver = silver

    def test_Purchase(self):
        merchant = Merchant()
        self.PopulateMerchantInventory(merchant)

        # Buying an item the merchant does not have
        p1 = Player()
        self.GivePlayerMoney(p1, 10, 0)
        result, resultString = p1.Purchase(merchant, "Does Not Exist")
        self.assertFalse(result)

        # Not enough coins for item
        p2 = Player()
        self.GivePlayerMoney(p2, 0, 0)
        for item in merchant.inventory.inventory.keys():
            result, resultString = p2.Purchase(merchant, item.name, 1)
            self.assertFalse(result)
            self.assertIn("Player does not have enough money", resultString)
            self.assertNotIn(item, p2.inventory.inventory)

        # Successful buying
        p3 = Player()
        self.GivePlayerMoney(p3, 100, 0)
        for item in merchant.inventory.inventory.keys():
            result, resultString = p3.Purchase(merchant, item.name, 1)
            self.assertTrue(result)
            self.assertIn(item, p3.inventory.inventory)

    def test_Sell(self):
        player = Player()
        self.PopulatePlayerInventory(player)

        # Item is not in player's inventory
        self.assertFalse(player.Sell("Does Not Exist")[0])

        # Item is in player's inventory, player sells all of the item
        items = list(player.inventory.inventory.items())
        for item, amount in items:
            result, resultString = player.Sell(item.name, amount)
            self.assertTrue(result)
            self.assertNotIn(player.inventory[item.name], player.inventory.inventory)

        # Selling one more than the player carries in their inventory
        self.PopulatePlayerInventory(player)
        for item, amount in items:
            print(item)
            result, resultString = player.Sell(item.name, amount + 1)
            self.assertFalse(result)
            self.assertIn(player.inventory[item.name], player.inventory.inventory)
            self.assertEqual(amount, player.inventory.inventory[player.inventory[item.name]])
