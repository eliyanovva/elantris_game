"""
Main module of the game.

"""

import json
import sys
from three_classes import Character


def exit_game(json_file):
    """
    The function closes the file and exits the program.
    """
    print('The game is over. Goodbye!')
    json_file.close()
    sys.exit()

if __name__=="__main__":

    with open("messages_data.json", "r") as file:
        data = json.load(file)

    INITIAL_LOCATION = 'Elantris'
    Ivan = Character(INITIAL_LOCATION)

    while True:

        print('\nPlease enter:\
              \n\'location\' to see the what you can do in your current location',
             '\n\'items\' to see what you can do with the items in your inventory, \
            \n\'all\' to see all possible options. \n')

        message_input = input()
        Ivan.print_options(data, message_input)

        print('\nPlease enter the number of the option you have chosen. \
               \nAdditional instructions:\n \
              \'bag\' to check the current contents of your bag, \n \
              \'pin\' to check your current location \n \
              \'q\' to exit the game.')

        input_str = input()

    #   TODO: invalid input, linting, testing

        if input_str == 'bag':
            Ivan.print_current_inventory()
            continue
        if input_str == 'pin':
            Ivan.print_current_location()
            continue
        if input_str in ('q', '13'):
            exit_game(file)

        if not input_str.isdigit():
            print('You have entered invalid input, please try again')
            continue
        input_int = int(input_str, 10)

        message = Ivan.find_message(input_int, data)
        Ivan.action_on_message(message, data)
