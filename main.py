from openai import OpenAI
import os
import requests
import random
from words import word_list

# consts
QUIT = 'Q'
BASE_URL = 'https://www.stands4.com/services/v2/defs.php?uid='
FORMAT = '&format=json'
QUIT_PROMPT = '(or press Q to quit)'
PROMPT = 'Define the word'

# vars
uid = '12640'
tokenid = 'jy5TWMF0mBZdg5Bv'
user_input = ''
current_word = 'consistent'
url = ''
count = 0

# functions


def useChatGPT(user_definition, word_to_define, actual_definition):

    my_api_key = os.getenv('OPENAI_KEY')

    client = OpenAI(
        api_key=my_api_key,
    )

    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are an english professor and" +
                " can identify whether a phrase is a good is " +
                "definition based on a provided definition."},
            {"role": "user", "content": "Is the following definition: " +
                user_definition +
                " a good definition of the word " + word_to_define +
                " ,based on the following definition: " + actual_definition +
                " and give the definition a grade" +
                " using the A-F grading scale."}
            ]
    )
    print(completion.choices[0].message.content)


def getNewWord(word_lst):
    # fill in
    new_word = random.choice(word_lst)
    word_lst.remove(new_word)
    return new_word


def getDefintion(word, uid, tokenid):
    # PEP warning being difficult
    url = BASE_URL + uid + "&tokenid=" + tokenid + "&word=" + word + FORMAT

    response = requests.get(url, headers={'User-Agent': 'curl/7.81.0'})

    definition = response.json()
    result = definition['result'][0]['definition']
    return result


while user_input != QUIT:

    # run a question
    current_word = getNewWord(word_list)

    # get user definition

    try:
        # PEP warning being difficult
        if count == 0:
            user_input = str(input(f'{PROMPT} {current_word} {QUIT_PROMPT}: '))
            count += 1
        else:
            print("\n")
            user_input = str(input(f'{PROMPT} {current_word} {QUIT_PROMPT}: '))

    except:
        # Error Catch
        print("how did you mess this up")

    # gives space between loop iterations
    print("\n")

    # prevent chatgpt from using "Q" as an input
    if user_input == QUIT:
        break

    # get actual definition

    current_definition = getDefintion(current_word, uid, tokenid)

    useChatGPT(user_input, current_word, current_definition)
