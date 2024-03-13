import os
import random

dir_path = os.path.dirname(os.path.realpath(__file__))

#Exercise 1 – Random Sentence Generator
file = '/words.txt'
def get_words_from_file(file):
    with open(dir_path+file) as f:
        content_list = f.readlines()
        content_words = []
        for word in content_list:
            content_words.append(word[:-1])
        return content_words


def get_random_sentence(length):
    sentence = []
    for i in range(length):
        sentence.append(random.choice(get_words_from_file(file)))
    sentence = ' '.join(sentence).lower().capitalize()+'.'
    return sentence


valid_length = [i for i in range(2,21)]

def main():
    print('This program will generate a random sentence\n',end='-------')
    length_of_sentance = input('How many words would you like to generate in a sentence?(from 2 to 20 words): ')

    if length_of_sentance.isdigit():
        length = int(length_of_sentance)
        if length not in valid_length:
            print('Please enter a number between 2 and 20')
        else:
            words = get_words_from_file(file)
            sentence = get_random_sentence(length)
            print(sentence)
    else:
        print('End of the program')
main()

#Exercise 2: Working With JSON

import json

sampleJson = """{ 
   "company":{ 
      "employee":{ 
         "name":"emma",
         "payable":{ 
            "salary":7000,
            "bonus":800
         }
      }
   }
}"""

json_object = json.loads(sampleJson)

#Add a key called “birth_date” to the JSON-string at the same level as the “name” key.
print(json_object['company']['employee']['payable']['salary'])

#Add a key called “birth_date” to the JSON-string at the same level as the “name” key.
json_object['company']['employee']['birth_date'] = '1999/07/09'

#Save the dictionary as JSON to a file.
with open(dir_path+'/sample.json', 'w') as f_obj:
    json.dump(json_object, f_obj, indent=2, sort_keys=True)






