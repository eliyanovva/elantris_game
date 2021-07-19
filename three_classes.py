# -*- coding: utf-8 -*-
"""
Created on Thu Jul  8 08:29:15 2021

@author: Teodora

"""


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
        self.__item_dict = {}

    def increment_item(self, item):
        """
        Input: Item key
        If the key exists in the dictionary, it is incremented with 1
        Otherwise, it is added to the dictionary
        """
        if item in self.__item_dict:
            self.__item_dict[item] += 1
        else:
            self.__item_dict[item] = 1

    def delete_item(self, item):
        """
        Input: Item key
        The value related to the key is decremented with 1
        """
        self.__item_dict[item] -= 1

    def message_update_items(self, message, item):
        """
        takes action upon a message from the json file
        currently, decrements with 1 the value of an item for some messages
        """
        if message['next_item_state'] == 0:
            self.delete_item(item)

    def get_inventory(self):
        """
        returns the dictionary
        """
        return self.__item_dict


class Location:
    """
    The class contains a location as a string

    It handles operations like:
        update location
        get location
    """

    def __init__(self, location):
        """
        Constructor of the class which initializes the location
        and the item dictionary.
        """
        self.__location = location

    def update_location(self, new_location, json_file):
        """
        Updates the location of the object and prints a welcome message.
        """
        if self.__location != new_location:
            print(json_file[new_location]['intro'])
        self.__location = new_location

    def get_location(self):
        """
        used to show the current location to the user
        """
        return self.__location


class Character:
    """
    The class performs the action of in the game.
    It has Location and Inventory attributes and updates them upon
    different user inputs.
    """
    def __init__(self, location):
        """
        Constructor of a character class which has a location and an inventory.
        The class which initializes the location and the item dictionary.
        """
        self.__inventory = Inventory()
        self.__location = Location(location)
        
    def print_current_location(self):
        """
        Prints the current location  of the character.
        """
        print('You are in ', self.__location.get_location())

    def print_current_inventory(self):
        """
        Prints the inventory of the character.
        """
        print('The contents of your bag are: ',
              self.__inventory.get_inventory())

    def __print_item_options(self, json_file):
        """
        Prints the messages related to the current state of the inventory.
        Every item's messages are specific for a certain location.
        """
        for item in self.__inventory.get_inventory():
            if self.__inventory.get_inventory().get(item) != 0:
                for j in json_file[self.__location.get_location()]['items'][item]:
                    print(j['string'], '\n')

    def __print_location_options(self, json_file):
        """
        Prints the message options which are related to the location of the object
        """
        for message in json_file[self.__location.get_location()]['locationMessages']:
            print(message['string'], '\n')

    def print_options(self, json_file, choice):
        """
        Prints all options, per the choice of the user.
        Asks for new input and calls itself again upon invalid input.
        """
        if choice == "location":
            self.__print_location_options(json_file)
        elif choice == "items":
            self.__print_item_options(json_file)
        elif choice == "all":
            self.__print_location_options(json_file)
            self.__print_item_options(json_file)
        else:
            print('Invalid input, try again')
            new_choice = input()
            self.print_options(json_file, new_choice)

    def __search_item_message(self, json_file, input):
        """
        Searches for a message related to an item which matches the input ID.
        Returns the message as a dictionary or an empty dictionary if no message
        matches the input ID.
        """
        message = {}
        json_dict = json_file[self.__location.get_location()]['items']
        for item in json_dict:
            for choice in json_dict[item]:
                if choice['ID'] == input:
                    message = choice
                    message['cur_item'] = item

        return message

    def __search_location_message(self, input, json_file):
        """
        Searches for a message related to a location which matches the input ID.
        Returns the message as a dictionary or an empty dictionary if no matching
        ID is found.
        """
        message = {}
        for choice in json_file[self.__location.get_location()]['locationMessages']:
            if choice['ID'] == input:
                message = choice
        return message

    def find_message(self, input, json_file):
        """
        Searches for a message which matches the input using
        the private item message and location message methods defined above.
        """
        message = self.__search_location_message(input, json_file)
        if message == {}:
            message = self.__search_item_message(json_file, input)
        return message

    def __action_location_message(self, message, json_file):
        """
        Gets a location message dictionary as input and updates the Location and the
        Inventory of the Character accordingly.
        """
        self.__location.update_location(message['next_state'], json_file)
        if message['new_item'] != '':
            self.__inventory.increment_item(message['new_item'])

    def __action_item_message(self, message, json_file):
        """
        Gets an item message dictionary as input and updates the Location and
        the Inventory of the Character accordingly.
        """
        self.__location.update_location(message['next_state'], json_file)
        if message['next_item_state'] != 1:
            self.__inventory.delete_item(message['cur_item'])

    def action_on_message(self, message, json_file):
        """
        Updates the Location and Inventory based on a message dictionary input.
        """
        if 'cur_item' in message.keys():
            self.__action_item_message(message, json_file)
        elif 'new_item' in message.keys():
            self.__action_location_message(message, json_file)
