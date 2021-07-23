import unittest
from location import *


class TestLocation(unittest.TestCase):
    def setUp(self) -> None:
        self.mod = Location()

    def tearDown(self) -> None:
        del self.mod
    
    def test_mod_is_instance(self):
        self.assertIsInstance(self.mod, Location)
    
    def test_set_location_valid_input(self):
        self.mod.set_location('Elantris')
        self.assertTrue(self.mod._location == 'Elantris')
     
    # have to use stub/mock for this function
    def test_update_location_valid_input(self):
        pass
    
    def test_update_location_invalid_json(self):
        pass
    
    def test_get_location_valid(self):
        self.mod._location = 'Elantris'
        self.assertEqual(self.mod.get_location(), 'Elantris')

    def test_get_location_none(self):
        self.assertRaises(LocationException, self.mod.get_location)