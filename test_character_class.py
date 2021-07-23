import unittest
from unittest.mock import patch, MagicMock
from character import *


class TestCharacter(unittest.TestCase):
    def setUp(self) -> None:
        self.mod = Character()

    def tearDown(self) -> None:
        del self.mod
    
    def test_mod_is_instance(self):
        self.assertIsInstance(self.mod, Character)
    
    def test_initialize_location_valid_location(self):
        json_dict = {'Available Places': ['Elantris', 'Kae']}
        self.mod.initialize_location('Elantris', json_dict)
        self.assertEqual('Elantris', self.mod._location._location)

    def test_initialize_location_location_not_in_json_dictionary(self):
        json_dict = {'Available Places':['Elantris', 'Kae']}
        self.assertRaises(CharacterException, self.mod.initialize_location, 'Teod', json_dict)
    
    def test_location_is_instance(self):
        json_file_dict = {'Available Places':['test']}
        self.mod.initialize_location('test', json_file_dict)
        self.assertIsInstance(self.mod._location, Location)
    
    def test_inventory_is_instance(self):
        self.mod.initialize_inventory()
        self.assertIsInstance(self.mod._inventory, Inventory)

    def test_set_name_valid(self):
        self.mod.set_name('Gosho')
        self.assertEqual(self.mod._name, 'Gosho')
    
    def test_set_type_valid(self):
        json_dict = {
            "Available Characters": ['Elantrian', 'Kae resident']
        }
        self.mod.set_type('Elantrian', json_dict)
        self.assertEqual(self.mod._type, 'Elantrian')

    def test_set_type_not_in_json_dictionary(self):
        json_dict = {
            "Available Characters": ['Elantrian', 'Kae resident']
        }
        self.assertRaises(CharacterException, self.mod.set_type, 'Dillaf', json_dict)

    @patch('builtins.print')
    def test_print_current_location(self, mock_print):
        self.mod.initialize_location('Elantris', {'Available Places':['Elantris']})
        self.mod.print_current_location()
        mock_print.assert_called_with('You are in ', 'Elantris')

    @patch('builtins.print')
    def test_print_current_inventory_empty(self, mock_print):
        self.mod.initialize_inventory()
        self.mod.print_current_inventory()
        mock_print.assert_called_with('The contents of your bag are: ', {})

    @patch('builtins.print')
    def test_print_current_inventory_nonempty(self, mock_print):
        self.mod.initialize_inventory()
        self.mod._inventory._item_dict = {'food':1, 'Beer':13, 'crown':2}
        self.mod.print_current_inventory()
        mock_print.assert_called_with('The contents of your bag are: ', {'food':1, 'Beer':13, 'crown':2})

    def test_obj_has_items_for_message_no_items_in_message_empty_inventory(self):
        message = {'needed_items':[]}
        self.assertTrue(self.mod._has_items_for_message(message))

    def test_obj_has_items_for_message_no_items_in_message_one_item_in_inventory(self):
        message = {'needed_items':[]}
        self.mod.initialize_inventory()
        self.mod._inventory._item_dict = {'food':1}
        self.assertTrue(self.mod._has_items_for_message(message))

    def test_obj_has_items_for_message_no_items_in_message_many_items_in_inventory(self):
        message = {'needed_items':[]}
        self.mod.initialize_inventory()
        self.mod._inventory._item_dict = {'food':1, 'water':2}
        self.assertTrue(self.mod._has_items_for_message(message))

    def test_obj_has_items_for_message_one_item_in_message_empty_inventory(self):
        message = {'needed_items':['food']}
        self.mod.initialize_inventory()
        self.mod._inventory._item_dict = {}
        self.assertFalse(self.mod._has_items_for_message(message))
        
    def test_obj_has_items_for_message_one_item_in_message_one_correct_item_in_inventory(self):
        message = {'needed_items':['food']}
        self.mod.initialize_inventory()
        self.mod._inventory._item_dict = {'food':1}
        self.assertTrue(self.mod._has_items_for_message(message))

    def test_obj_has_items_for_message_one_item_in_message_one_incorrect_item_in_inventory(self):
        message = {'needed_items':['food']}
        self.mod.initialize_inventory()
        self.mod._inventory._item_dict = {'water':1}
        self.assertFalse(self.mod._has_items_for_message(message))

    def test_obj_has_items_for_message_one_item_in_message_many_correct_items_in_inventory(self):
        message = {'needed_items':['food']}
        self.mod.initialize_inventory()
        self.mod._inventory._item_dict = {'food':5}
        self.assertTrue(self.mod._has_items_for_message(message))

    def test_obj_has_items_for_message_one_item_in_message_many_correct_and_incorrect_items_in_inventory(self):
        message = {'needed_items':['food']}
        self.mod.initialize_inventory()
        self.mod._inventory._item_dict = {'food':5, 'water':1, 'terminal': 14}
        self.assertTrue(self.mod._has_items_for_message(message))
    
    def test_obj_has_items_for_message_one_item_in_message_many_incorrect_items_in_inventory(self):
        message = {'needed_items':['food']}
        self.mod.initialize_inventory()
        self.mod._inventory._item_dict = {'water':5, 'books':14}
        self.assertFalse(self.mod._has_items_for_message(message))


    def test_obj_has_items_for_message_many_items_in_message_empty_inventory(self):
        message = {'needed_items':['food', 'water']}
        self.mod.initialize_inventory()
        self.mod._inventory._item_dict = {}
        self.assertFalse(self.mod._has_items_for_message(message))

    def test_obj_has_items_for_message_many_items_in_message_one_correct_item_in_inventory(self):
        message = {'needed_items':['food', 'water']}
        self.mod.initialize_inventory()
        self.mod._inventory._item_dict = {'food':1}
        self.assertFalse(self.mod._has_items_for_message(message))

    def test_obj_has_items_for_message_many_items_in_message_one_correct_and_many_incorrect_items_in_inventory(self):
        message = {'needed_items':['food', 'water']}
        self.mod.initialize_inventory()
        self.mod._inventory._item_dict = {'food':1, 'galoshi':13, 'trotinetki':12}
        self.assertFalse(self.mod._has_items_for_message(message))

    def test_obj_has_items_for_message_many_items_in_message_many_correct_items_in_inventory(self):
        message = {'needed_items':['food', 'water']}
        self.mod.initialize_inventory()
        self.mod._inventory._item_dict = {'food':12, 'water':12}
        self.assertTrue(self.mod._has_items_for_message(message))

    def test_obj_has_items_for_message_many_items_in_message_many_correct_and_many_incorrect_items_in_inventory(self):
        message = {'needed_items':['food', 'water']}
        self.mod.initialize_inventory()
        self.mod._inventory._item_dict = {'warer':14, 'food':2, 'galoshi':13, 'trotinetki':12}
        self.assertFalse(self.mod._has_items_for_message(message))
    
    def test_obj_is_type_for_message_type_is_allowed_and_message_is_open_to_one(self):
        json_data_dict = {'Available Characters': ['Elantrian', 'Kae resident']}
        self.mod.set_type('Elantrian', json_data_dict)
        message = {'open to':['Elantrian']}
        self.assertTrue(self.mod._is_type_for_message(message))

    def test_obj_is_type_for_message_type_is_allowed_and_message_is_open_to_many(self):
        json_data_dict = {'Available Characters': ['Elantrian', 'Kae resident']}
        self.mod.set_type('Elantrian', json_data_dict)
        message = {'open to':['Elantrian', 'Kae resident']}
        self.assertTrue(self.mod._is_type_for_message(message))

    def test_obj_is_type_for_message_type_not_allowed_and_message_is_open_to_one(self):
        json_data_dict = {'Available Characters': ['Elantrian', 'Kae resident']}
        self.mod.set_type('Kae resident', json_data_dict)
        message = {'open to':['Elantrian']}
        self.assertFalse(self.mod._is_type_for_message(message))

    def test_obj_is_type_for_message_type_not_allowed_and_message_is_open_to_many(self):
        json_data_dict = {'Available Characters': ['Elantrian', 'Kae resident', 'Dillaf', 'Harathen']}
        self.mod.set_type('Elantrian', json_data_dict)
        message = {'open to':['Harathen', 'Dillaf']}
        self.assertFalse(self.mod._is_type_for_message(message))

    def test_can_access_message_obj_not_message_type_no_items_for_message(self):
        message = {}
        self.mod._is_type_for_message = MagicMock(return_value = False)
        self.mod._has_items_for_message = MagicMock(return_value = False)
        self.assertFalse(self.mod._can_access_message(message))

    def test_can_access_message_obj_is_message_type_no_items_for_message(self):
        message = {}
        self.mod._is_type_for_message = MagicMock(return_value = True)
        self.mod._has_items_for_message = MagicMock(return_value = False)
        self.assertFalse(self.mod._can_access_message(message))

    def test_can_access_message_obj_not_message_type_has_items_for_message(self):
        message = {}
        self.mod._is_type_for_message = MagicMock(return_value = False)
        self.mod._has_items_for_message = MagicMock(return_value = True)
        self.assertFalse(self.mod._can_access_message(message))

    def test_can_access_message_obj_is_message_type_has_items_for_message(self):
        message = {}
        self.mod._is_type_for_message = MagicMock(return_value = True)
        self.mod._has_items_for_message = MagicMock(return_value = True)
        self.assertTrue(self.mod._can_access_message(message))

    @patch('builtins.print')
    def test_print_options_can_print_all(self):
        # export data away from test fucntion / extra file
        # export to additional class, change setup and teardown functions
        json_data_dict = {
        "Available Places": ["Elantris"],
        "Available Characters": ["Elantrian"],
        "Elantris": {
		"messages":	[
			{
				"needed_items": [],
				"string": "1: Feels like the hunger is catching up on me, I'd better search for some woed newcomer's food.", 
				"open to": ["Elantrian"]
			},
			{
				"needed_items":["food"],
				"string": "4: I am so hungry, I want to eat right now!",
				"open to": ["Elantrian", "Kae resident"]
			},
		]
        }}
        self.mod.initialize_location('Elantris', json_data_dict)
        self.mod.initialize_inventory()
        self.mod._inventory._item_dict = {'food':12}
        self.mod.set_type('ELantrian', json_data_dict)
        self.mod.print_options(json_data_dict)
        #mock_print.assert_called_with('The contents of your bag are: ', {'food':1, 'Beer':13, 'crown':2})
