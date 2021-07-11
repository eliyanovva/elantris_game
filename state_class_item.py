# -*- coding: utf-8 -*-
"""
Created on Thu Jul  8 08:29:15 2021

@author: Teodora
"""

# item_arr: food, book, clothes
# items are stored as bools in the Character class, each new state acts in a certain way to an object.
# add empty stuff / check if key exists in line 32

class Character:
    """ 
    The class has attributes location of type string and item_dict of type dictionary. It describes the location and the current inventory of the game Character.
    """
    
    # change constructor 
    def __init__(self, location, item_dict):
        """ 
        Constructor of the class which initializes the location and the item dictionary. 
        """
        self.__location = location
        self.__item_dict = item_dict
    
    def update_location(self, new_location, json_file):
        """
        Updates the location of the object and prints a welcome message. Should not be used to update to the same location.
        """
        self.__location = new_location
        print(json_file[self.__location]['intro'])
    
    def print_location_options(self, json_file):
        """
        Prints the message options which are related to the location of the object
        """
        for i in json_file[self.__location]['locationMessages']:
            print(i['string'], '\n')
    
    def print_item_options(self, json_file):
        """
        Prints the messages which are related to the current state of the inventory of the object. The item-location relationship is specified in the JSON file, not here. Every item message is specific for a certain location.
        """
        for i in self.__item_dict:
            if self.__item_dict.get(i)!=0:
                for j in json_file[self.__location]['items'][i]:
                    print(j['string'], '\n')
                    
    def see_inventory(self):
        """
        used to show the current state of the inventory to the user
        """
        print(self.__item_dict)
        
    def see_location(self):
        """
        used to show the current location to the user
        """
        print('You are in ', self.__location)   
    	
    def update_loc_options(self, input, json_file):
        """
        input is of type int
        the function searches for the message with the same ID as the input in the location related messages. Then, the location and the inventory of the object are updated according to the matching message.
        """
        for choice in json_file[self.__location]['locationMessages']:
            if choice['ID'] == input and choice['next_state']!= self.__location:
                self.update_location(choice['next_state'], json_file)
            
            if choice['ID'] == input and choice['next_item_state'] != "" and self.__item_dict[choice['next_item_state']]==0:
                self.__item_dict[choice['next_item_state']] = 1

    def update_item_options(self, input, json_file):
        """
        input is of type int
        the function searches for the message with the same ID as the input in the item-location related messages. The location and the inventory of the object are updated according to the matching message.
        """
        for item in json_file[self.__location]['items']:
            for choice in json_file[self.__location]['items'][item]:
                if choice['ID'] == input and choice['next_state']!=self.__location:
                    self.update_location(choice['next_state'], json_file)
                if choice['ID'] == input and choice['next_item_state']==0:
                    self.__item_dict[item] = 0
