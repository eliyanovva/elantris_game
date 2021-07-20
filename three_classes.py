# -*- coding: utf-8 -*-
"""
Created on Thu Jul  8 08:29:15 2021

@author: Teodora

"""

class ElantrianException(Exception):
    pass

class KaeCitizenException(Exception):
    pass

class Inventory:
    """
    The class contains a dictionary of items and their quantities

    It handles operations like:
        add item
        remove item
        action on an item based on a message from json file
        get dictionary
    """
    def __init__(self):
        """The contructor initilizes an empty dictionary"""
        self._item_dict = {}

    def increment_item(self, item):
        """
        Input: Item key
        If the key exists in the dictionary, it is incremented with 1
        Otherwise, it is added to the dictionary
        """
        if item in self._item_dict:
            self._item_dict[item] += 1
        else:
            self._item_dict[item] = 1

    def delete_item(self, item):
        """
        Input: Item key
        The value related to the key is decremented with 1
        """
        self._item_dict[item] -= 1
        if self._item_dict[item] == 0:
            self._item_dict.pop(item)

    def get_inventory(self):
        """
        returns the dictionary
        """
        return self._item_dict


class Location:
    """
    The class contains a location as a string

    It handles operations like:
        update location
        get location
    """

    def __init__(self):
        """
        Constructor of the class which initializes the location
        and the item dictionary.
        """
        self._location = None
    
    def set_location(self, location):
        self._location = location

    def update_location(self, new_location, json_file):
        """
        Updates the location of the object and prints a welcome message.
        """
        if self._location != new_location:
            print(json_file[new_location]['intro'])
        self.set_location(new_location)

    def get_location(self):
        """
        used to show the current location to the user
        """
        return self._location


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

    def initialize_location(self, new_location):
        self._location = Location()
        self._location.set_location(new_location)
    
    def initialize_inventory(self):
        self._inventory = Inventory()
    
    def set_name(self, name):
        self._name = name
    
    def set_type(self, type):
        self._type = type
    
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

    def _can_access_message(self, message):
        return self._type in message['open to'] and (message['needed_items']==[] or \
        set(message['needed_items']).issubset(set(self._inventory.get_inventory()))) 

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
        for new_item in message['add_items']:
            self._inventory.increment_item(new_item)
        for removed_item in message['delete_items']:
            self._inventory.delete_item(removed_item)


class ElantrianCharacter(Character):
    """
    The class inherits the Character class. Its initial location
    is 'Elantris.'
    """
    def __init__(self):
        """
        Constructor of Elantris Character class which inherits the Character class.
        The Elantrian starts with an empty inventory and in Elantris.
        """
        try:
            super(ElantrianCharacter, self).__init__()
        except:
            raise ElantrianException('The Elantrian Character class did not initialize properly')
        
        self.initialize_location('Elantris')
        self.initialize_inventory()
        self.set_type('Elantrian')


class KaeCitizenCharacter(Character):
    """
    The class inherits the Character clas. Its initial location is Kae.
    """
    def __init__(self):
        try:
            super(KaeCitizenCharacter, self).__init__()
        except:
            raise KaeCitizenException('The Kae Citizen Character class did not initialize properly')
        
        self.initialize_location('Kae')
        self.initialize_inventory()
        self.set_type('Kae resident')



import json
with open("messages_data.json", "r") as file:
    data = json.load(file)

Ivan = KaeCitizenCharacter()
Ivan.set_name('Ivan')

Ivan.print_options(data)
