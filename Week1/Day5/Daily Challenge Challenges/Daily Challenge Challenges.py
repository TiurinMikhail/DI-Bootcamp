#Daily Challenge Challenges

#Challenge 1 : Sorting

#without,hello,bag,world

def sorting_words(*words):
    words_list = list(words)
    words_list.sort()
    print(','.join(words_list))


sorting_words('without', 'hello', 'bag', 'world')

#Challenge 2 : Longest Word
def longest_word(sentence):
    len_longest = 0
    longest_words_list = []
    sentence = sentence.replace('.', '').replace('?', '').replace('!', '').replace('...', '').replace(',', '').replace(';', '').replace(':', '')
    list_of_words = [i for i in sentence.split()]
    for i in range(len(list_of_words)):
        if len(list_of_words[i]) >= len_longest:
            len_longest = len(list_of_words[i])
            longest_words_list.append(list_of_words[i])
    if len(longest_words_list) > 1:
        if len(longest_words_list[-1]) == len(longest_words_list[-2]):
            print(longest_words_list[-2])
        else:
            print(longest_words_list[-1])
    else:
        print(longest_words_list[-1])


longest_word("Forgetfulness is by all means Forgggfulness!")
