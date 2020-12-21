import unittest
from Characters.Merchant import Merchant
from Objects.Item import Item


class TestMerchant(unittest.TestCase):
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

    def test_SellWare(self):
        merchant = Merchant()
        self.PopulateMerchantInventory(merchant)

        # Item is not in merchant's inventory
        self.assertIsNone(merchant.SellWare("Does Not Exist"))

        # Item is in merchant's inventory
        for item in merchant.inventory.inventory.keys():
            self.assertEqual(item, merchant.SellWare(item.name))
