from openai import OpenAI
import os
import requests
import random

# consts
QUIT = 'Q'
BASE_URL = 'https://www.stands4.com/services/v2/defs.php'

# vars
uid = '12640'
tokenid = 'jy5TWMF0mBZdg5Bv'
user_input = ''
current_word = 'consistent'
url = ''

# functions


def useChatGPT(definition, word_to_define):

    my_api_key = os.getenv('OPENAI_KEY')

    client = OpenAI(
        api_key=my_api_key,
    )

    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are an english professor and" +
                " can identify words based on their definitions."},
            {"role": "user", "content": "Is the following phrase a good" +
                " definition of the word " + word_to_define + " :" +
                definition}
            ]
    )
    print(completion.choices[0].message.content)


def getNewWord(word_list):
    # fill in
    """
    Purpose: to get a random new word
    1) select a random word from word_list
    2) delete selected word from word_list
    3) return the selected word
    """

# PEP warning being difficult
url = "https://www.stands4.com/services/v2/defs.php?uid=" + uid + "&tokenid=" + tokenid + "&word=" + current_word + "&format=json"

response = requests.get(url, headers={'User-Agent': 'curl/7.81.0'})


if response.status_code == 200:
    print(response.json())
else:
    print(response.status_code)

while user_input != QUIT:

    # run another question

    try:
        # PEP warning being difficult
        user_input = str(input(f'Define the word {current_word} (or press Q to quit): '))

    except:
        # Error Catch
        print("how did you mess this up")

    # useChatGPT(user_input, current_word)
