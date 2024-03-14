from anagram_checker import AnagramChecker

def show_user_menu():
    print("Welcome to anagram checker!")
    while True:
        print('     MENU\n', '(i) Input a word to find all anagrams\n', '(x) Exit\n')
        choice = input('Enter your choice: ')
        if choice == 'i':
            words = AnagramChecker()
            while True:
                user_input = input('Enter your word: ')
                user_input = user_input.strip()
                user_check = user_input.split()
                if len(user_check) == 1 and all(char.isalpha() for char in user_check):
                    break
                else:
                    print('Invalid input entered. Try again.')
            print(f'\nYour word: "{user_input}"')
            result = words.get_anagrams(user_input)
            if result == 'This word is not valid':
                print('This word is not valid\n')
            else:
                print('this is a valid English word')
                if len(result) == 0:
                    print('There is no anagram for this word!')
                else:
                    print(f'Here is the list of anagrams for {user_input}:', ', '.join(result))
                    print()
        elif choice == 'x':
            break
    print('Thank you for using this program!')

show_user_menu()

