from openai import OpenAI
import os

QUIT = 'Q'

user_input = ""

current_word = 'mors'

def useChatGPT(definition, word_to_define):

	my_api_key = os.getenv('OPENAI_KEY')

	client = OpenAI(
    	api_key=my_api_key,
	)

	completion = client.chat.completions.create(
		model="gpt-3.5-turbo",
		messages=[
			{"role": "system", "content": "You are an english professor and can identify words based on their definitions."},
			{"role": "user", "content": "Is the following phrase a good definition of the word " + word_to_define + " :" + definition}
		]
	)
	print(completion.choices[0].message.content)



while user_input != QUIT:

    #run another question

    try:
        user_input = str(input(f'Define the word {current_word} (or press Q to quit): '))

    except:
        #redundant
        #user_input = input(f'test: ')
        #user_input = input(f'Define the word {current_word}: ')
		# we need something here
        print("how did you mess this up")

    useChatGPT(user_input, current_word)
    

"""

"""

#Request URL
#https://www.stands4.com/services/v2/defs.php