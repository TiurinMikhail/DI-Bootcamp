import os
import string
dir_path = os.path.dirname(os.path.realpath(__file__))

import nltk
from nltk.corpus import stopwords

nltk.download('stopwords')
nltk.download()

stop_words = set(stopwords.words('english'))

############################################################

class Text:
    def __init__(self, string):
        self.string = string

    def __str__(self):
        return self.string

    def word_frequency(self,word):
        list_of_words = self.string.replace('.', '').lower().split()
        frequency = list_of_words.count(word)
        if frequency == 0:
            print(f"The word '{word}' does not appear in the text.")
            return None
        else:
            print(f"The word '{word}' appears {frequency} times in the text.")
            return frequency

    def most_common_words(self):
            frequencies = {}
            list_of_words = self.string.replace('.', '').lower().split()
            for word in list_of_words:
                frequencies[word] = list_of_words.count(word)
            most_common = ''
            freq = 1
            for key, value in frequencies.items():
                if value > freq:
                    most_common = key
                    freq = value
            if freq > 1:
                return most_common
            else:
                return 'All of the words in the text appears only once!'

    def unic_words(self):
        frequencies = {}
        list_of_words = self.string.replace('.', '').replace('\n',' ').lower().split()
        for word in list_of_words:
            frequencies[word] = list_of_words.count(word)
        unic_words = []
        for key, value in frequencies.items():
            if value == 1:
                unic_words.append(key)
        return unic_words

    @classmethod
    def from_file(cls,file_name):
        with open(dir_path+file_name, 'r') as f:
            text = f.readlines()
            text = ' '.join(text)
        return cls(text)

    def remove_punctuation(self):
        punctuation = string.punctuation
        text = ''.join(char for char in self.string if char not in punctuation)
        return text


    def remove_stopwords(self,stop_words):
        text = self.remove_punctuation().lower().split()
        text_final = ' '.join(word for word in text if word not in stop_words)
        return text_final



text1 = Text('A good book would sometimes cost as much as a good house.')

text1.word_frequency('fox')
most_common_word = text1.most_common_words()
unic_words = text1.unic_words()
print(most_common_word)
print(unic_words)
print(text1)

file_text = Text.from_file('/the_stranger.txt')

file_text.word_frequency('good')
most_common_file_word = file_text.most_common_words()
print(most_common_file_word)
unic_file_words = file_text.unic_words()
print(unic_file_words)


#print(file_text.remove_punctuation())
print(file_text.remove_stopwords(stop_words))



