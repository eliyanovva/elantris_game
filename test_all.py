import unittest
from test_character_class import TestCharacter
from test_inventory_class import TestInventory
from tests_location_class import TestLocation

if __name__ == '__main__':
    test_location = TestLocation()
    test_inventory = TestInventory()
    test_character = TestCharacter()
    unittest.main()
    