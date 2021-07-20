"""
Main module of the game.

"""

import json
import sys
from three_classes import ElantrianCharacter, KaeCitizenCharacter


def exit_game(json_file):
    """
    The function closes the file and exits the program.
    """
    print('The game is over. Goodbye!')
    json_file.close()
    sys.exit()


def start_game():
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
        game_character = ElantrianCharacter()
    elif type == 'k':
        game_character = KaeCitizenCharacter()
    else:
        print('Please pick a valid character')
        start_game()

    game_character.set_name(name)
    
    return game_character


if __name__ == "__main__":

    User = start_game()

    with open("messages_data.json", "r") as file:
        data = json.load(file)

    while True:

        User.print_options(data)

        print('\nPlease enter the number of the option you have chosen. \
               \nAdditional instructions:\n \
              \'bag\' to check the current contents of your bag, \n \
              \'pin\' to check your current location \n \
              \'q\' to exit the game.')

        input_str = input()

    #   TODO: fix death at perpendicularity lake, invalid input, testing

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
        User.action_on_message(message, data)
