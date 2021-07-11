from state_class_item import Character
import json
import string

def exit_game(json_file):
    print('The game is over. Goodbye!')
    json_file.close()
    exit(0)

with open("messages_data.json", "r") as file:
    data = json.load(file)
    
init_state= 'Elantris'
init_dict = {'food':0, 'book':0, 'clothes':0}

Ivan = Character(init_state, init_dict)

while True:
   
    print('\nPlease enter the number of the option you have chosen.\nAdditional instructions:\n\"q\" --  quit the game\n\"items\" -- check your backpack\n\"location\" -- check your current location\n')

    ### search for location and item options with separate threads ###
    Ivan.print_location_options(data)
    Ivan.print_item_options(data)
    
    input_str =input()
    
    if input_str=='q' or input_str=='13':
        exit_game(file)

    if input_str == 'items':
       Ivan.see_inventory()
       continue
    if input_str == 'location':
       Ivan.see_location()
       continue
       
    input_int = int(input_str, 10)
### try catch for bad input, disallow python code input ###
### update loc and item options with separate threads ###
    Ivan.update_loc_options(input_int, data)
    Ivan.update_item_options(input_int, data)
    
