import random as r

word_list = ['correction', 'childish', 'beach', 'python', 'assertive', 'interference', 'complete', 'share', 'credit card', 'rush', 'south']


def get_word(word_list):
    word = r.choice(word_list).upper()
    return word


def display_hangman(tries):
    stages = [  # final state: head, torso, both arms, both legs
        '''
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     / \\
           -
        ''',
        # head, torso, both arms, one leg
        '''
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     / 
           -
        ''',
        # head, torso, both arms
        '''
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |      
           -
        ''',
        # head, torso, one arm
        '''
           --------
           |      |
           |      O
           |     \\|
           |      |
           |     
           -
        ''',
        # head and torso
        '''
           --------
           |      |
           |      O
           |      |
           |      |
           |     
           -
        ''',
        # head
        '''
           --------
           |      |
           |      O
           |    
           |      
           |     
           -
        ''',
        # initial empty state
        '''
           --------
           |      |
           |      
           |    
           |      
           |     
           -
        '''
    ]
    return stages[tries]


# Writing a function to open letters
def reveal(word_completion, sp, letter):
    word_list = list(word_completion)
    for i in sp:
        word_list[i] = letter
    word_completion = ''.join(word_list)
    return word_completion


# Protection from stupidity
def is_valid(strk):
    strk_1 = strk.strip()
    if strk_1.isalpha():
        return True
    else:
        return False


def play(word):
    # function body
    print('Let\'s play a word guessing game!')
    dl_slv = len(word)
    word_completion = '_' * len(word)  # string containing _ characters for each letter of the guessed word
    guessed = False  # signal mark
    guessed_letters = []  # list of already guessed letters
    guessed_words = []  # list of already guessed words
    tries = 6  # number of attempts
    print(f'Number of attempts:{tries} {display_hangman(tries)}')
    print(f'Guess the word: {word_completion} with {dl_slv} letters')
    while guessed == False:
        user_input = input('Enter the word or a letter: ').upper().strip()
        if user_input == word:
            guessed = True
            print('Congratulations, you guessed the word! You won!')
            break
        if is_valid(user_input):
            # Adding a check for the presence of a word (letter) in the lists used earlier
            if user_input in guessed_letters or user_input in guessed_words:
                print('You have already guessed this letter (word)! Try another one.')
            else:
                # Adding a word (letter) to the list of already used ones
                if len(user_input) == 1:
                    guessed_letters.append(user_input)
                elif len(user_input) > 1:
                    guessed_words.append(user_input)
                # Checking for a match in letters or words
                if user_input in word:
                    if len(user_input) == 1:
                        sp_ind = []
                        for i in range(len(word)):
                            if word[i] == user_input:
                                sp_ind.append(i)
                        word_completion = reveal(word_completion, sp_ind, user_input)
                        print(word_completion)
                        sp_ind = []
                else:
                    tries -= 1
                    print(f'Tries left: {tries}')
                    print(display_hangman(tries))
                if tries == 0 and "_" in word_completion:
                    guessed = True
                    print(f'You lost. The word was: {word}')
                    break
                elif word_completion == word:
                    guessed = True
                    print('Congratulations, you guessed the word! You won!')
                    break
        else:
            print('Enter only letters or the word! You cannot enter numbers')


again = 'y'

while again.lower() == 'y':
    word = get_word(word_list)
    play(word)
    again = input('Let\'s try again? (y = yes, n = no): ').lower().strip()
    if again == 'n' or again == 'no':
        print('Thanks for playing the word guessing game. See you again...')