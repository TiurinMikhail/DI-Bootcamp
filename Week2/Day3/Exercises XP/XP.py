#Exercise 1: Currencies
class Currency:
    def __init__(self, currency, amount):
        self.currency = currency
        self.amount = amount

    def __str__(self):
        return f'{self.amount} {self.currency}s'

    def __int__(self):
        return int(round(self.amount, 0))

    def __repr__(self):
        return f'{self.amount} {self.currency}s'

    def __add__(self, other):
        if isinstance(other, Currency) and self.currency == other.currency:
            return self.amount + other.amount
        elif isinstance(other, Currency) and self.currency != other.currency:
            raise TypeError(f'Cannot add between Currency type {self.currency} and {other.currency}')

        else:
            return self.amount + other

    def __iadd__(self, other):
        if isinstance(other, Currency) and self.currency == other.currency:
             self.amount += other.amount
             return self
        elif isinstance(other, Currency) and self.currency != other.currency:
             raise TypeError(f'Cannot add between Currency type {self.currency} and {other.currency}')

        else:
             self.amount += other
             return self


c1 = Currency('dollar', 5)
c2 = Currency('dollar', 10)
c3 = Currency('shekel', 1)
c4 = Currency('shekel', 10)
c5 = Currency('dollar', 5.6)


print(c5)
print(int(c5))
print(c5+0.5)

print(str(c1))
print(int(c1))
print(repr(c1))
print('-----')
print(c1+5)

print(c1+c2)

print(c1)

c1 += 5
print('----')
print(c1)

c1 += c2
print(c1)

#c1 + c3


#Exercise 3: String Module

import random as rd

import string

stroke = string.ascii_letters

def random_string(length):
    random_string = ''
    for i in range(length):
        random_string += rd.choice(stroke)
    print(random_string)

random_string(5)

# Exercise 4 : Current Date

import datetime as datetime

def current_date():
    current_date =  datetime.datetime.now()
    formatted_date = current_date.strftime("%Y-%m-%d")
    return formatted_date

print(f'Today: {current_date()}')

#Exercise 5 : Amount Of Time Left Until January 1st

def time_till():
    current_date = datetime.datetime.now()
    january_1st_2025 = datetime.datetime(2025, 1, 1, 0, 0)
    time_till_1st_2025 = january_1st_2025-current_date
    days = time_till_1st_2025.days
    hours, remainder = divmod(time_till_1st_2025.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    print(f"The 1st of January is in {days} days and {hours:02d}:{minutes:02d}:{seconds:02d} hours.")

time_till()


#Exercise 6 : Birthday And Minutes

from datetime import datetime

def minutes_from_birth():
    date = input("Please enter your birthday (dd/mm/yyyy format): ")
    birthday = datetime.strptime(date, "%d/%m/%Y")
    current_date = datetime.now()
    difference = current_date - birthday
    difference_in_minutes = difference.total_seconds() / 60
    print(f'I live {difference.days} days, {round(difference_in_minutes,2)} minutes')

minutes_from_birth()

#Exercise 7 : Faker Module


from faker import Faker

faker = Faker()

users = []

def add_user():
    user = {
    'name': faker.name(),
    'address': faker.address(),
    'language_code': faker.language_code()
    }
    users.append(user)

for _ in range(40):
    add_user()

for user in users:
    for key, value in user.items():
        print(f'{key}: {value}')
    print('------')

