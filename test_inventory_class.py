import unittest
from inventory import *


class TestInventory(unittest.TestCase):
    def setUp(self) -> None:
        self.mod = Inventory()

    def tearDown(self) -> None:
        del self.mod
    
    def test_mod_is_instance(self):
        self.assertIsInstance(self.mod, Inventory)
    
    def test_increment_item_key_doesnt_exist(self):
        self.mod.increment_item('food')
        self.assertEqual(self.mod._item_dict['food'], 1)

    def test_increment_item_key_exists(self):
        self.mod._item_dict['food'] = 3
        self.mod.increment_item('food')
        self.assertDictEqual(self.mod._item_dict, {'food':4})
    
    def test_delete_item_key_doesnt_exist(self):
        self.assertRaises(InventoryException, self.mod.delete_item, 'item')

    def test_delete_item_key_value_greater_than_1(self):
        self.mod._item_dict['food'] = 5
        self.mod.delete_item('food')
        self.assertEqual(self.mod._item_dict['food'], 4)
    
    def test_delete_item_key_value_equal_to_1(self):
        self.mod._item_dict['food'] = 1
        self.mod.delete_item('food')
        self.assertFalse(set(['food']).issubset(set(self.mod._item_dict)))

    def test_get_inventory(self):
        self.mod._item_dict = {'food':1, 'book':2}
        self.assertEqual(self.mod.get_inventory(), {'food':1, 'book':2})
