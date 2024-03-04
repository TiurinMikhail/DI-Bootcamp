#Exercise 1: Concatenate Lists
list1 = [1,2,3,4,5,6,7,8]
list2 = [1,2,3,4,5,6,7,8]
list1.extend(list2)
print(list1)

#Exercise 2: Range Of Numbers
for i in range(1500,2501):
    if i % 5 == 0 and i % 7 == 0:
        print(i)

#Exercise 3: Check The Index
names = ['Samus', 'Cortana', 'V', 'Link', 'Mario', 'Cortana', 'Samus']
user_name = input('Enter your name: ')
if user_name in names:
    print(names.index(user_name))

#Exercise 4: Greatest Number
list_num = []
first_number = int(input('Enter first number: '))
list_num.append(first_number)
second_number = int(input('Enter second number: '))
list_num.append(second_number)
third_number = int(input('Enter third number: '))
list_num.append(third_number)
print(max(list_num))

#or
list_num = []
for i in range(3):
    number = int(input('Enter number: '))
    list_num.append(number)
print(max(list_num))

#Exercise 5: The Alphabet
string = 'qwertyuiopasdfghjklzxcvbnm'
vowel = 'euoia'
for letter in string:
    if letter in vowel:
        print(f'The letter {letter} is vowel')
    else:
        print(f'The letter {letter} is consonant')

#Exercise 6: Words And Letters
words = []
for i in range(7):
    words.append(input('Enter a word: ').lower())
letter = input('Enter only one letter: ')
for word in words:
    if letter in word:
        print(word.find(letter))
    else:
        print(f'Oh, it is Okay! Letter {letter} does not in {word}')

#Exercise 7:
one_to_mln = [i for i in range(1,1000001)]
print('Min is '+str(min(one_to_mln)),'Max is '+str(max(one_to_mln)),sep='\n')
print(sum(one_to_mln)) #python calculate it very fast

#Exercise 8 : List And Tuple
numbers = [int(i) for i in input('Enter numbers: ').split(',')]
tup = tuple(numbers)
print(numbers,tup,sep='\n')

#Exercise 9 : Random Number
import random

guessed_number = random.randint(1, 10)

print('Welcome to the number guessing game!')

# Foolproof check: the entered string should not contain letters, and the number in the string should be in the range from 1 to 100 inclusive.
def is_valid(str):
    list_num = [num for num in range(1, 101)]
    if str.isdigit():
        if int(str) in list_num:
            return True
        else:
            return False
    else:
        return False

print('Enter the upper limit for randomly choosing a number from 1 to n')
n = input()
right_bounder = int(n)

# Main program loop
fin_num = 0
again = 'y'
won = 0
lose = 0
while again.lower() == 'y':
    guessed_number = random.randint(1, right_bounder)
    while guessed_number != fin_num:
        user_input = input('Enter your number! ')
        if is_valid(user_input):
            fin_num = int(user_input)
            if fin_num != guessed_number:
                print('Your number is not rigth, try again later!')
                lose += 1
                break
            else:
                print('Winner!')
                won += 1
        else:
            print(f'How about entering an integer from 1 to {right_bounder}?')
    again = input('Want to try again? (y = yes, n = no): ')
print(f'You have {won} wins snd {lose} loses.')
print('Thanks for playing the number guessing game. See you again...',)

#Version 2.0
import random

guessed_number = random.randint(1, 100)

print('Welcome to the number guessing game!')

# Foolproof check: the entered string should not contain letters, and the number in the string should be in the range from 1 to 100 inclusive.
def is_valid(str):
    list_num = [num for num in range(1, 101)]
    if str.isdigit():
        if int(str) in list_num:
            return True
        else:
            return False
    else:
        return False

print('Enter the upper limit for randomly choosing a number from 1 to n')
n = input()
right_bounder = int(n)

# Main program loop
fin_num = 0
again = 'y'
while again.lower() == 'y':
    cnt = 0
    guessed_number = random.randint(1, right_bounder)
    while guessed_number != fin_num:
        user_input = input('Enter your number! ')
        if is_valid(user_input):
            fin_num = int(user_input)
            if fin_num < guessed_number:
                print('Your number is less than the guessed one, try again')
                cnt += 1
            elif fin_num > guessed_number:
                print('Your number is greater than the guessed one, try again')
                cnt += 1
            else:
                cnt += 1
                print(f'You guessed the number, congratulations! Number of attempts = {cnt}')
        else:
            print('How about entering an integer from 1 to 100?')
    again = input('Want to try again? (y = yes, n = no): ')
print('Thanks for playing the number guessing game. See you again...')