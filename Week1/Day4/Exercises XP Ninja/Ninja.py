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

#Exercise 3 : Box Of Stars
