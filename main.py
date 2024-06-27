from openai import OpenAI
import os
import requests
import random
from words import word_list
import sqlite3


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
current_grade = ''
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
                " and give the definition a grade using the A-F grading scale" +
                " in the format of Grade: *Grade* on a new Line." +
				" Make sure to have the grade be after the explanation."}
            ]
    )

    output = completion.choices[0].message.content
    print(output)

    tmp = output[-2:]
    grade = ""

    for letter in tmp:
        if letter.isalnum():
            grade += letter

    return grade


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


# setting up the database
conn = sqlite3.connect('gradebook.db')
c = conn.cursor()
c.execute('''
    CREATE TABLE IF NOT EXISTS results (
    questionNumber INTEGER PRIMARY KEY,
    word TEXT NOT NULL,
    actualDef TEXT,
    Grade CHAR
    )
''')


while user_input != QUIT:

    # run a question
    current_word = getNewWord(word_list)

    # get user definition

    if count == 0:
        user_input = str(input(f'{PROMPT} {current_word} {QUIT_PROMPT}: '))
        count += 1
    else:
        print("\n")
        user_input = str(input(f'{PROMPT} {current_word} {QUIT_PROMPT}: '))
        count += 1

    # gives space between loop iterations
    print("\n")

    # prevent chatgpt from using "Q" as an input
    if user_input == QUIT:
        break

    # get actual definition

    current_definition = getDefintion(current_word, uid, tokenid)

    # send to chatGPT

    current_grade = useChatGPT(user_input, current_word, current_definition)

    # append everything to the database
    c.execute('''
        INSERT INTO results (questionNumber, word, actualDef, grade )
        VALUES (?, ?, ?, ?)
    ''', (count, current_word, current_definition, current_grade)
    )

c.execute(
    'SELECT * FROM results'
)
print(f"{'Question':<15}{'Word':<15}{'Grade':<10}")
data = c.fetchall()
for rows in data:
    num = str(rows[0])
    word = str(rows[1])
    definition = str(rows[2])
    grade = str(rows[3])
    print(f"{num:<15}{word:<15}{grade:<10}")

conn.close()
