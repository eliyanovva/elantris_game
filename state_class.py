# -*- coding: utf-8 -*-
"""
Created on Thu Jul  8 08:29:15 2021

@author: Teodora
"""

#import dictionaries from the other file here?
# dict_locs - the dictionary which maps the message IDs to a location
#dict_items - dictionary which maps items to message IDs
#dict_messages - dictionary which maps messages to message IDs

# Items are stored in a list

dict_locs = {1:'Elantris', 2:'Elantris', 5:'Kae'} # keep as list of loc names instead
dict_items = {18:'food', 25:'book'}

items = {
    "book": {
        "options": {
            "Elantris": ["1: asd"],
            "Kae": ["1: asd"]
        },
        "color": {
            "Elantris": "red",
            "Kae": "green"
        }
    },
    "cup": {
        "options": {
            "Elantris": ["1: asd"],
            "Kae": ["1: asd"]
        }
    }
}


class Location:
    def __init__(self, new_loc_name, current_loc_name):
        self.name = new_loc_name
        self.options_list = [i for i, j in dict_locs.items()
                        if j==new_loc_name]
        self.previous_name = current_loc_name;
   
    

class Item:
    def __init__(self, name, item_id):
        self.name = name
        self.id = item_id
        self.options_list =  [i for i, j in dict_items.items()
                        if j==name]
        self.options_list = items[name][character.location]
        #                  items['book']['Elantris'] => list
    
# add character class
         
