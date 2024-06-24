from openai import OpenAI
import os

QUIT = 'Q'

user_input = ""

current_word = 'mors'

while user_input != QUIT:

    #run another question

    try:
        user_input = str(input(f'Define the word {current_word}: '))

    except:
        #redundant
        #user_input = input(f'test: ')
        #user_input = input(f'Define the word {current_word}: ')



#Request URL
#https://www.stands4.com/services/v2/defs.php