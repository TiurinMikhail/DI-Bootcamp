#Exercise 1 : When Will I Retire ?
from datetime import datetime

def get_age(year, month, day):
    today = datetime.today()
    current_year = today.year
    current_month = today.month
    current_day = today.day
    age = current_year - year - ((current_month, current_day) < (month, day))
    return age

def can_retire(gender, date_of_birth):
    date_of_birth = datetime.strptime(date_of_birth, '%d/%m/%Y')
    age = get_age(date_of_birth.year, date_of_birth.month, date_of_birth.day)
    if (gender.lower() == 'm' and age >= 67) or (gender.lower() == 'f' and age >= 62):
        return True
    else:
        return False

user_date = input("Enter your Date of Birth: ")
user_gender = input("Enter your gender (f=female,m=male): ")

print(can_retire(user_gender, user_date))

#Exercise 2 : Sum
def sum_digits(x):
    summ = 0
    list_sum = [str(x)*i for i in range(1,5)]
    for i in list_sum:
        summ += int(i)
    return summ

print(sum_digits(3))


# Exercise 3 : Double Dice
import random

def throw_dice():
    return random.randint(1,6)

def throw_until_doubles():
    a = throw_dice()
    b = throw_dice()
    cnt_throw = 1
    if a != b:
        while a != b:
            a = throw_dice()
            b = throw_dice()
            cnt_throw += 1
    return cnt_throw

def main():
    total_throws = []
    for i in range(100):
        cnt = throw_until_doubles()
        total_throws.append(cnt)
    print(f'It took {sum(total_throws)} throws to reach 100 doubles.')
    print(f'The average amount of throws is {round(sum(total_throws)/len(total_throws),2)}')

main()