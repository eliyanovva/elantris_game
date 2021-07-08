# -*- coding: utf-8 -*-
"""
Created on Thu Jul  8 08:29:15 2021

@author: Teodora
"""

# item_arr: food, book, clothes
# items are stored as bools in the Character class, each new state acts in a certain way to an object.

import json

with open("messages_data.json", "r") as file:
    data = json.load(file)

#print(data)

class Character:        
    def __init__(self, location, item_list, print_intro):
        self.location = location
        self.item_list = item_list
        if print_intro != 0:
            print(data[self.location]['intro'])
        
        
    def print_options(self):
        for i in data[self.location]['locationMessages']:
            print(i['string'])
            

init_state= 'Elantris'
init_items = [0,0,0]
Ivan = Character(init_state, init_items, 1)

while True:
   
    print('\n Please enter the number of the option you have chosen, or press \"q\" if you want to quit:\n')
   
    Ivan.print_options() 
    input_str = input()
    
    if input_str=='q' or input_str=='13':
       break
   
    new_location = ''
    
    for i in data[Ivan.location]['locationMessages']:
        if i['ID'] == int(input_str, 10):
            new_location = i['next_state']
    
    intro_flag =0
    if new_location!=Ivan.location:
        intro_flag = 1            
    Ivan = Character(new_location, init_items, intro_flag)


file.close()