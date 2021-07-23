"""
Main module of the game.

"""

import json
import sys
from character import CharacterException, ElantrianCharacter, KaeCitizenCharacter


def exit_game(json_file):
    """
    The function closes the file and exits the program.
    """
    print('The game is over. Goodbye!')
    json_file.close()
    sys.exit()


def start_game(json_file_dict):
    """
    The function starts the game by initializing 
    a Character class.
    """
    print('Hello! Please, pick your character: \
        \n Elantrian: you have been hit by the Sheod a few days ago,\
        \nand you are slowly adjsuting to your new lifestyle in Elantris.\
        \n Choose this character by pressing \'e\'.\n')
    print('\nKae Resident: you are the best spice merchant in town!\
        \nUnfortunately, king Iadon hates you for that, and wishes you dead.\
        \nYou have joined the nobles\' opposition meetings recently.\
        \nChoose this character by pressing \'k\'')
    type = input()
    print('Please enter the name of your character!')
    name = input()
    if type == 'e':
        game_character = ElantrianCharacter(json_file_dict)
    elif type == 'k':
        game_character = KaeCitizenCharacter(json_file_dict)
    else:
        print('Please pick a valid character')
        start_game()

    game_character.set_name(name)
    
    return game_character


if __name__ == "__main__":

    with open("elantris_game-main/messages_data.json", "r") as file:
        data = json.load(file)
   
    User = start_game(data)

    while True:

        User.print_options(data)

        print('\nPlease enter the number of the option you have chosen. \
               \nAdditional instructions:\n \
              \'bag\' to check the current contents of your bag, \n \
              \'pin\' to check your current location \n \
              \'q\' to exit the game.')

        input_str = input()

        if input_str == 'bag':
            User.print_current_inventory()
            continue
        if input_str == 'pin':
            User.print_current_location()
            continue
        if input_str in ('q'):
            exit_game(file)

        if not input_str.isdigit():
            print('You have entered invalid input, please try again')
            continue
        input_int = int(input_str, 10)

        message = User.search_message(data, input_int)
        try:
            User.action_on_message(message, data)
        except(CharacterException):
            exit_game(file)
        # TODO: change logic to search only when printing, then store messages
        # then choose action from the ones stored 
        # pros: validate only upon first search, only one searching
        # cons: memory storage of messages (not too many messages will be stored, which makes up for the extra search)
