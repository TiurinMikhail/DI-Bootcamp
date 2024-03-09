#Exercise 1 : What’s Your Name ?
def get_full_name(first_name, last_name, middle_name=''):
    if middle_name == '':
        return first_name.capitalize() + ' ' + last_name.capitalize()
    else:
        return ' '.join([first_name.capitalize(), middle_name.capitalize(), last_name.capitalize()])

print(get_full_name(first_name="john", middle_name="hooker", last_name="lee"))
print(get_full_name(first_name="bruce", last_name="lee"))


#Exercise 2 : From English To Morse

morse_dict = {
    'A': '.-',    'B': '-...',  'C': '-.-.', 'D': '-..',   'E': '.',    'F': '..-.', 'G': '--.',
    'H': '....',  'I': '..',    'J': '.---', 'K': '-.-',   'L': '.-..', 'M': '--',   'N': '-.',
    'O': '---',   'P': '.--.',  'Q': '--.-', 'R': '.-.',   'S': '...',  'T': '-',    'U': '..-',
    'V': '...-',  'W': '.--',   'X': '-..-', 'Y': '-.--',  'Z': '--..'
}

sentence = input("Enter a sentence: ")

def convert_morse(word):
    for letter in sentence:
        if letter.isalpha():
            print(morse_dict.get(letter.capitalize())+' ',end='')
        elif letter == ' ':
            print('/',end='')

convert_morse(sentence)
print()
#Exercise 3 : Box Of Stars
def longest_word(user_array):
    longest_word = ''
    for word in user_array:
        if len(word) > len(longest_word):
            longest_word = word
    return longest_word

def box_printer(*strings):
    string_list = []
    for el in strings:
        string_list.append(el)
    lngst_word = longest_word(string_list)
    print('*'*(len(lngst_word)+4))
    for el in string_list:
        if el != lngst_word:
            print('* '+el+' '*(len(lngst_word)-len(el)-2)+'   *')
        else:
            print('* ' + el + ' ' * (len(lngst_word) - len(el) - 2) + ' *')
    print('*'*(len(lngst_word)+4))

box_printer("Hello", "World", "in", "reallylongword", "a", "frame")

#Exercise 4- Analyse this code before executing it. What is the purpose of this code?

#The purpose of this code is to demonstrate the insertion sort algorithm by sorting a given list of numbers
