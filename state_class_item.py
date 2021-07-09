# -*- coding: utf-8 -*-
"""
Created on Thu Jul  8 08:29:15 2021

@author: Teodora
"""

# item_arr: food, book, clothes
# items are stored as bools in the Character class, each new state acts in a certain way to an object.
# add empty stuff / check if key exists in line 32
import json

with open("messages_data.json", "r") as file:
    data = json.load(file)


class Character:
    """ put docstrings """
    # change constructor 
    def __init__(self, location, item_dict, print_intro):
        self.location = location
        self.item_dict = item_dict
        if print_intro != 0:
            print(data[self.location]['intro'])
    
    #change location - print_intro
    # update inventory
        
    def print_location_options(self):
        for i in data[self.location]['locationMessages']:
            print(i['string'], '\n')
    
    def print_item_options(self):
        for i in self.item_dict:
            if self.item_dict.get(i)!=0:
                for j in data[self.location]['items'][i]:
                    print(j['string'], '\n')
    
    def see_inventory(self):
        print(self.item_dict)    

        
init_state= 'Elantris'
init_dict = {'food':0, 'book':0, 'clothes':0}
Ivan = Character(init_state, init_dict, 1)

while True:
   
    print('\n Please enter the number of the option you have chosen, or press \"q\" if you want to quit:\n')
   
    Ivan.print_location_options()
    Ivan.print_item_options()
    
    input_str = input()
    
    if input_str=='q' or input_str=='13':
       # create function for exit
       break
   
    new_location = ''
    item_dict = Ivan.item_dict
    
    # put in separate functions
    # change i, j to something with meaning
    
    for i in data[Ivan.location]['locationMessages']:
        if i['ID'] == int(input_str, 10):
            new_location = i['next_state']
            if i['next_item_state'] != "" and item_dict[i['next_item_state']]==0:
                item_dict[i['next_item_state']] = 1
    
    for i in data[Ivan.location]['items']:
        for j in data[Ivan.location]['items'][i]:
            if j['ID'] == int(input_str, 10):
                new_location = j['next_state']
                if j['next_item_state']==0:
                    item_dict[i] = 0
    
    intro_flag =0
    if new_location!=Ivan.location:
        intro_flag = 1   
    Ivan.see_inventory()     
    Ivan = Character(new_location, item_dict, intro_flag)


file.close()

# make backpack class, inherit character from it
