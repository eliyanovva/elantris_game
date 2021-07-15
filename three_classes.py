# -*- coding: utf-8 -*-
"""
Created on Thu Jul  8 08:29:15 2021

@author: Teodora

TODO: move search message to Character, merge the behaviour of the two functions
      print options too!
"""


class Inventory:
    """
    The class contains a dictionary of items and their quantities
    
    It handles operations like:
        add item
        remove item
        print contents of the inventory
    """
    def __init__(self):
        """The contructor initilizes an empty dictionary"""
        self.__item_dict={}

    def print_item_options(self, json_file, location):
        """
        Prints the messages which are related to the current state of the inventory.
        Every item's messages are specific for a certain location.
        """
        for i in self.__item_dict:
            if self.__item_dict.get(i) != 0:
                for j in json_file[location]['items'][i]:
                    print(j['string'], '\n')

    def update_items(self, item):
        if item in self.__item_dict:
            self.__item_dict[item] += 1
        else:
            self.__item_dict[item] = 1

    def delete_item(self, item):
        self.__item_dict[item] -= 1

    def search_message(self, json_file, input_ID, location):
        message = {}
        for item in json_file[location]['items']:
            for choice in json_file[location]['items'][item]:
                if choice['ID'] == input_ID:
                    message = choice
                    message['cur_item'] = item
        
        return message

    def message_update_items(self, message, item):
        if message['next_item_state'] == 0:
            self.delete_item(self, item)  

    def get_inventory(self):
        """
        used to show the current state of the inventory to the user
        """
        return(self.__item_dict)              
                    

class Location:
    """ 
    The class has attributes location of type string and item_dict of type dictionary.
    It describes the location and the current inventory of the game Character.
    """
    
    # change input to json file, where location is set to the first location, item_dict is set to the items listed
    def __init__(self, location):
        """ 
        Constructor of the class which initializes the location and the item dictionary. 
        """
        self.__location = location

    def print_location_options(self, json_file):
        """
        Prints the message options which are related to the location of the object
        """
        for i in json_file[self.__location]['locationMessages']:
            print(i['string'], '\n')

    def update_location(self, new_location, json_file):
        """
        Updates the location of the object and prints a welcome message. Should not be used to update to the same location.
        """
        if self.__location != new_location:
            print(json_file[new_location]['intro'])
        self.__location = new_location
        
    def get_location(self):
        """
        used to show the current location to the user
        """
        return self.__location   

    def search_message(self, input, json_file):
        """
        input is of type int
        the function searches for the message with the same ID as the input in the location related messages.
        Then, the location and the inventory of the object are updated according to the matching message.
        """
        message = {}
        for choice in json_file[self.__location]['locationMessages']:
            if choice['ID'] == input:

                message = choice
        return message 


class Character:
    def __init__(self, location):
        """ 
        Constructor of the class which initializes the location and the item dictionary. 
        """
        self.__inventory = Inventory()
        self.__location = Location(location)
    
    def print_current_location(self):
        print('You are in ', self.__location.get_location())
    
    def print_current_inventory(self):
        print('The contents of your bag are: ', self.__inventory.get_inventory())

    def print_options(self, json_file, choice):
        if choice == "location":
            self.__location.print_location_options(json_file)
        elif choice == "items":
            self.__inventory.print_item_options(json_file, self.__location.get_location())
        elif choice == "all":
            self.__location.print_location_options(json_file)
            self.__inventory.print_item_options(json_file, self.__location.get_location())
        else:
            print('Invalid input, try again')
            self.print_options(json_file)

    def find_message(self, input, json_file):
        message = self.__location.search_message(input, json_file)
        if message == {}:
            message = self.__inventory.search_message(json_file, input, self.__location.get_location())
        return message

    def action_location_message(self, message, json_file):
        self.__location.update_location(message['next_state'], json_file)
        if message['new_item'] != '':
            self.__inventory.update_items(message['new_item'])

    def action_item_message(self, message, json_file):
        self.__location.update_location(message['next_state'], json_file)
        if message['next_item_state'] != 1:
            self.__inventory.delete_item(message['cur_item'])

    def action_on_message(self, message, json_file):
        if 'cur_item' in message.keys():
            self.action_item_message(message, json_file)
        elif 'new_item' in message.keys():
            self.action_location_message(message, json_file)