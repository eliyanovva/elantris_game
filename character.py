"""
The Character factory class is stored here.
"""

from location import Location
from inventory import Inventory


class CharacterException(Exception):
    pass


class ElantrianException(CharacterException):
    pass


class KaeCitizenException(CharacterException):
    pass

class Character:
    """
    The class performs the action of in the game.
    It has Location and Inventory attributes and updates them upon
    different user inputs.
    """
    def __init__(self):
        """
        Constructor of a character class which has a location and an inventory.
        The class which initializes the location and the item dictionary.
        """
        self._inventory = None
        self._location = None
        self._name = ''
        self._type = ''

    def initialize_location(self, new_location, json_file_dict):
        self._location = Location()
        if new_location in json_file_dict['Available Places']:
           self._location.set_location(new_location)
        else:
            raise CharacterException('Invalid character location')
    
    def initialize_inventory(self):
        self._inventory = Inventory()
    
    def set_name(self, name):
        self._name = name
    
    def set_type(self, type, json_file_dict):
        if type in json_file_dict['Available Characters']:
            self._type = type
        else:
            raise CharacterException('Invalid character type')

    def print_current_location(self):
        """
        Prints the current location  of the character.
        """
        print('You are in ', self._location.get_location())

    def print_current_inventory(self):
        """
        Prints the inventory of the character.
        """
        print('The contents of your bag are: ',
              self._inventory.get_inventory())

    def _has_items_for_message(self, message):
        return message['needed_items']==[] or \
        set(message['needed_items']).issubset(set(self._inventory.get_inventory()))
    
    def _is_type_for_message(self, message):
        return self._type in message['open to']

    def _can_access_message(self, message):
        return self._has_items_for_message(message) and self._is_type_for_message(message)

    def print_options(self, json_file):
        for message in json_file[self._location.get_location()]['messages']:
            if self._can_access_message(message):
                print(message['string'], '\n')

    def search_message(self, json_file, input):
        for message in json_file[self._location.get_location()]['messages']:
            if self._can_access_message(message) and message['ID'] == input:
                return message

    def action_on_message(self, message, json_file):
        """
        Updates the Location and Inventory based on a message dictionary input.
        """
        self._location.update_location(message['next_state'], json_file)
        if self._location.get_location() == "Dead":
            raise CharacterException('Character is dead!')
        for new_item in message['add_items']:
            self._inventory.increment_item(new_item)
        for removed_item in message['delete_items']:
            self._inventory.delete_item(removed_item)


class ElantrianCharacter(Character):
    """
    The class inherits the Character class. Its initial location
    is 'Elantris.'
    """
    def __init__(self, json_file_dict):
        """
        Constructor of Elantris Character class which inherits the Character class.
        The Elantrian starts with an empty inventory and in Elantris.
        """
        try:
            super(ElantrianCharacter, self).__init__()
        except:
            raise ElantrianException('The Elantrian Character class did not initialize properly')
        
        self.initialize_location('Elantris', json_file_dict)
        self.initialize_inventory()
        self.set_type('Elantrian', json_file_dict)


class KaeCitizenCharacter(Character):
    """
    The class inherits the Character clas. Its initial location is Kae.
    """
    def __init__(self, json_file_dict):
        try:
            super(KaeCitizenCharacter, self).__init__()
        except:
            raise KaeCitizenException('The Kae Citizen Character class did not initialize properly')
        
        self.initialize_location('Kae', json_file_dict)
        self.initialize_inventory()
        self.set_type('Kae resident', json_file_dict)
