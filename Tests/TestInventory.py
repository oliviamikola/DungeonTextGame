import unittest
from Objects.Inventory import Inventory
from Objects.Item import Item
from Helpers.MaxTracker import MaxTracker


class TestInventory(unittest.TestCase):
    def CreateInventory(self, numItems: int, numStackable: int) -> Inventory:
        i = Inventory()
        m = MaxTracker(10)
        m.adjustable = numItems
        i.size = m
        for count in range(numStackable):  # Creating all the stackable items
            i.inventory[self.CreateStackableItem()] = count + 1
        for _ in range(numItems - numStackable):  # Creating all the unstackable items
            i.inventory[self.CreateUnstackableItem()] = 1
        return i

    def CreateStackableItem(self):
        return Item()

    def CreateUnstackableItem(self):
        item = Item()
        item.isStackable = False
        return item

    def test_clear(self):
        for size in range(11):  # The 11 here is the max size of the inventory
            # All stackable
            i1 = self.CreateInventory(size, size)
            i1.Clear()
            self.assertEqual(i1.inventory, {})
            self.assertEqual(i1.GetSize(), 0)

            # All unstackable
            i2 = self.CreateInventory(size, 0)
            i2.Clear()
            self.assertEqual(i2.inventory, {})
            self.assertEqual(i2.GetSize(), 0)

            # Mixed stackable and unstackable
            i3 = self.CreateInventory(size, size // 2)
            i3.Clear()
            self.assertEqual(i3.inventory, {})
            self.assertEqual(i3.GetSize(), 0)

    def test_add(self):
        for size in range(11):
            # Only adding stackable items
            i1 = self.CreateInventory(size, size)
            i1Items = i1.inventory.keys()
            for item in i1Items:
                previousSize = i1.GetSize()
                previousItemCount = i1.inventory[item]
                result = i1.Add(item)
                self.assertTrue(result)
                self.assertEqual(previousSize, i1.GetSize())
                self.assertEqual(previousItemCount + 1, i1.inventory[item])

            # Only adding unstackable items
            i2 = self.CreateInventory(size, 0)
            i2Items = i2.inventory.keys()
            for index, item in enumerate(i2Items):
                previousSize = i2.GetSize()
                previousItemCount = i2.inventory[item]
                result = i2.Add(item)
                if index + size + 1 <= 10:
                    self.assertTrue(result)
                    self.assertEqual(previousSize + 1, i2.GetSize())
                    self.assertEqual(previousItemCount + 1, i2.inventory[item])
                else:
                    self.assertFalse(result)
                    self.assertEqual(previousSize, i2.GetSize())
                    self.assertEqual(previousItemCount, i2.inventory[item])

            # Adding a mix of items
            i3 = self.CreateInventory(size, size // 2)
            i3Items = i3.inventory.keys()
            addedStackables = 0
            for index, item in enumerate(i3Items):
                previousSize = i3.GetSize()
                previousItemCount = i3.inventory[item]
                result = i3.Add(item)
                if item.isStackable:
                    addedStackables += 1
                    self.assertTrue(result)
                    self.assertEqual(previousSize, i3.GetSize())
                    self.assertEqual(previousItemCount + 1, i3.inventory[item])
                else:
                    if index + size + 1 - addedStackables <= 10:
                        self.assertTrue(result)
                        self.assertEqual(previousSize + 1, i3.GetSize())
                        self.assertEqual(previousItemCount + 1, i3.inventory[item])
                    else:
                        self.assertFalse(result)
                        self.assertEqual(previousSize, i3.GetSize())
                        self.assertEqual(previousItemCount, i3.inventory[item])

    def test_remove(self):
        for size in range(11):
            # Removing from inventory with only stackable items
            i1 = self.CreateInventory(size, size)
            i1Items = list(i1.inventory.keys())
            for item in i1Items:
                startSize = i1.GetSize()
                startCount = i1.inventory[item]
                for numRemoved in range(startCount - 1):
                    result = i1.Remove(item)
                    self.assertTrue(result)
                    self.assertEqual(startCount - numRemoved - 1, i1.inventory[item])
                    self.assertEqual(startSize, i1.GetSize())
                result = i1.Remove(item)
                self.assertTrue(result)
                self.assertNotIn(item, i1.inventory)
                self.assertEqual(startSize - 1, i1.GetSize())
                result = i1.Remove(item)  # item is no longer in the inventory, so this should be false
                self.assertFalse(result)
                self.assertNotIn(item, i1.inventory)
                self.assertEqual(startSize - 1, i1.GetSize())

            # Removing from inventory with only unstackable items
            i2 = self.CreateInventory(size, 0)
            i2Items = list(i2.inventory.keys())
            for item in i2Items:
                startSize = i2.GetSize()
                result = i2.Remove(item)
                self.assertTrue(result)
                self.assertNotIn(item, i2.inventory)
                self.assertEqual(startSize - 1, i2.GetSize())
                result = i2.Remove(item)  # item is no longer in the inventory, so this should be false
                self.assertFalse(result)
                self.assertNotIn(item, i2.inventory)
                self.assertEqual(startSize - 1, i2.GetSize())

            # Removing from inventory with mixed items
            i3 = self.CreateInventory(size, size // 2)
            i3Items = list(i3.inventory.keys())
            for item in i3Items:
                startSize = i3.GetSize()
                if item.isStackable:
                    startCount = i3.inventory[item]
                    for numRemoved in range(startCount - 1):
                        result = i3.Remove(item)
                        self.assertTrue(result)
                        self.assertEqual(startCount - numRemoved - 1, i3.inventory[item])
                        self.assertEqual(startSize, i3.GetSize())
                    result = i3.Remove(item)
                    self.assertTrue(result)
                    self.assertNotIn(item, i3.inventory)
                    self.assertEqual(startSize - 1, i3.GetSize())
                    result = i3.Remove(item)  # item is no longer in the inventory, so this should be false
                    self.assertFalse(result)
                    self.assertNotIn(item, i3.inventory)
                    self.assertEqual(startSize - 1, i3.GetSize())
                else:
                    result = i3.Remove(item)
                    self.assertTrue(result)
                    self.assertNotIn(item, i3.inventory)
                    self.assertEqual(startSize - 1, i3.GetSize())
                    result = i3.Remove(item)  # item is no longer in the inventory, so this should be false
                    self.assertFalse(result)
                    self.assertNotIn(item, i3.inventory)
                    self.assertEqual(startSize - 1, i3.GetSize())
