# Exercise 1 : What Are You Learning ?
def display_message():
    print('I am learning functions in python today!')


display_message()


# Exercise 2: What’s Your Favorite Book ?
def favorite_book(title):
    print(f'One of my favorite books is {title}')


favorite_book('Harry Potter')


# Exercise 3 : Some Geography
def describe_city(name='Washington', country='USA'):
    print(f'{name} is in {country}')


describe_city('Moscow', 'Russia')
describe_city()

# Exercise 4 : Random
import random as rd


def compare_rd_numbers(number):
    rand_number = rd.randint(1, 100)
    if rand_number == number:
        print('Success!')
    else:
        print('Fail!', number, rand_number)


compare_rd_numbers(50)


# Exercise 5 : Let’s Create Some Personalized Shirts !
def make_shirt(size, message_text):
    print(f"The size of the shirt is {size} and the text is '{message_text}'")


make_shirt('Medium', 'Nice')

#4
def make_shirt(size = 'Large', message_text='I love Python” by default.'):
    print(f"The size of the shirt is {size} and the text is '{message_text}'")
#5
make_shirt()

#6
make_shirt('Medium')

#7
make_shirt('Small', 'Very Small')


# Exercise 6 : Magicians …
magician_names = ['Harry Houdini', 'David Blaine', 'Criss Angel']


def show_magicians(list_of_names):
    print(', '.join(list_of_names))


show_magicians(magician_names)

make_great = lambda name: f'The Great {name}'

magician_names = list(map(make_great, magician_names))
make_great(magician_names)
show_magicians(magician_names)

# Exercise 7 : Temperature Advice

import random as rand
#1

month_by_season = {'winter':[12,1,2], 'spring':[3,4,5], 'summer':[6,7,8], 'autumn':[9,10,11]}

def determine_season(month):
    for season,monthes in month_by_season.items():
        if month in monthes:
            return season


def get_random_temp():
    user_month_num = int(input('Enter the number of months: '))
    season = determine_season(user_month_num)
    if season == 'winter':
        return rand.uniform(-25, 5)
    elif season == 'spring':
        return rand.uniform(-5,16)
    elif season == 'summer':
        return rand.uniform(16,40)
    elif season == 'autumn':
        return rand.uniform(0,22)


def main():
    current_temperature = get_random_temp()
    print(f'The current temperature is {current_temperature} degrees Celsius.')
    if current_temperature < 0:
        print("Brrr, that's freezing! Wear some extra layers today!")
    elif current_temperature >= 0  and current_temperature < 16:
        print("Quite chilly! Don’t forget your coat")
    elif current_temperature >= 16 and current_temperature <= 23:
        print("It's warm enough! ")
    elif current_temperature > 23 and current_temperature <32:
        print("It's really warm outside!")
    else:
        print("It's hot!!")
main()

#5
# added a uniform()

#6
#added
#def determine_season(month):
    #for season,monthes in month_by_season.items():
       # if month in monthes:
           # return season


#Exercise 8 : Star Wars Quiz
data = [
    {
        "question": "What is Baby Yoda's real name?",
        "answer": "Grogu"
    },
    {
        "question": "Where did Obi-Wan take Luke after his birth?",
        "answer": "Tatooine"
    },
    {
        "question": "What year did the first Star Wars movie come out?",
        "answer": "1977"
    },
    {
        "question": "Who built C-3PO?",
        "answer": "Anakin Skywalker"
    },
    {
        "question": "Anakin Skywalker grew up to be who?",
        "answer": "Darth Vader"
    },
    {
        "question": "What species is Chewbacca?",
        "answer": "Wookiee"
    }
]

def print_cor_incor(num1,num2):
    print(f'The nuber of correct answers is {num1} and the nuber of incorrect answers is {num2}')

def get_question():
    cnt_incorrect = 10
    while cnt_incorrect > 3:
        cnt_correct = 0
        cnt_incorrect = 0
        wrong_answers = []
        wrong_questions = []
        answer_for_question = []
        for items in data:
            print(items['question'])
            user_answer = input('What is your answer?: ')
            if user_answer.lower() == items['answer'].lower():
                cnt_correct += 1
                print_cor_incor(cnt_correct, cnt_incorrect)
            else:
                cnt_incorrect +=1
                wrong_answers.append(user_answer)
                wrong_questions.append(items['question'])
                answer_for_question.append(items['answer'])
                print_cor_incor(cnt_correct, cnt_incorrect)
        for i in range(cnt_incorrect):
            print(f'You answered wrong: {wrong_questions[i]}. Your incorrect answer was {wrong_answers[i]}. The right answer is: {answer_for_question[i]}')
        print('Lets play again!')
    print('Thanks for playing!')
get_question()





