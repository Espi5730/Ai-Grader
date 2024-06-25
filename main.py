from openai import OpenAI
import os
import requests
import random

#consts
QUIT = 'Q'
BASE_URL = 'https://www.stands4.com/services/v2/defs.php'

#vars
uid = '12640'
tokenid = 'jy5TWMF0mBZdg5Bv'
user_input = ''
current_word = 'consistent'
url = ''
# f'https://www.stands4.com/services/v2/defs.php?uid={uid}&tokenid={tokenid}&word={current_word}&format=json'
url = 'https://www.stands4.com/services/v2/defs.php?uid=12640&tokenid=jy5TWMF0mBZdg5Bv&word=consistent&format=json'
response = requests.get(url)

#https://www.definitions.net/api.php
curl "https://www.stands4.com/services/v2/defs.php?uid=12639&tokenid=ovesI5sOYp2iUjQu&word=consistent&format=json"


##example https://www.stands4.com/services/v2/defs.php?uid=1001&tokenid=tk324324&word=consistent&format=xml
if response.status_code == 200:
    print(response.json())
else:
    print(response.status_code)

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

    # useChatGPT(user_input, current_word)
    

"""
{
	"results": {
		"result": {
			"term": "consistent, uniform",
			"definition": "the same throughout in structure or composition",
			"partofspeech": "adj",
			"example": "bituminous coal is often treated as a consistent and homogeneous product"
		}
	}
}

"""

#Request URL
#https://www.stands4.com/services/v2/defs.php