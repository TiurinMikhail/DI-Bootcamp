import os
import json
import nltk
# from itertools import permutations

dir_path = os.path.dirname(os.path.realpath(__file__))

# print(len(set(nltk.corpus.words.words())))

class AnagramChecker:
    def __init__(self):
        with open(dir_path+'/sowpods.txt', 'r') as f:
            text = f.read()
            text = text.split('\n')
        self.text = text

    def is_valid_word(self, word):
        return word.upper() in self.text

    def is_anagram(self, word1, word2):
        return sorted(word1.lower()) == sorted(word2.lower()) and word1 != word2
        # list_of_letters = list(word1)
        # all_combination = permutations(list_of_letters)
        # list_of_combinations = [''.join(all_combination) for all_combination in all_combination]
        # if word2 in list_of_combinations:
        #     return True
        # else:
        #     return False

    def get_anagrams(self, user_word):
        dic_of_anagrams = {user_word:[]}
        if self.is_valid_word(user_word):
            for word in self.text:
                if len(word) == len(user_word):
                    if self.is_anagram(user_word, word.lower()):
                        dic_of_anagrams[user_word].append(word.lower())
        else:
            return f'This word is not valid'
        return dic_of_anagrams[user_word]

# text1 = AnagramChecker()
# print(text1.text[0:25])
# print(text1.get_anagrams('meat'))