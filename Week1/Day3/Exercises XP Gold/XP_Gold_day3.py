#Exercise 1: Birthday Look-Up
birthdays = {
    "Alice": "1995/03/15",
    "Bob": "1990/08/21",
    "Charlie": "1988/11/04",
    "David": "2000/05/10",
    "Eve": "1992/12/28"
}

print("Welcome! You can look up the birthdays of the people in the list!")

person_name = input("Whose birthday would you like to know? ____ ")
birthday = input("What is his birthday? ____ ")

print(f'{person_name} was born in {birthday}!')

#Exercise 2: Birthdays Advanced
birthdays = {
    "Alice": "1995/03/15",
    "Bob": "1990/08/21",
    "Charlie": "1988/11/04",
    "David": "2000/05/10",
    "Eve": "1992/12/28"
}

print("Welcome! You can look up the birthdays of the people in the list!")
print(f'You can choose from this list of persons:\n', ", ".join(birthdays.keys()))

person_name = input("Whose birthday would you like to know? ____ ")
birthday = birthdays.get(person_name)

# Print out the birthday with a nicely-formatted message
if birthday:
    print(f"The birthday of {person_name} is: {birthday}")
else:
    print(f"Sorry, we don't have the birthday for {person_name}.")

#Exercise 3: Add Your Own Birthday

birthdays = {
    "Alice": "1995/03/15",
    "Bob": "1990/08/21",
    "Charlie": "1988/11/04",
    "David": "2000/05/10",
    "Eve": "1992/12/28"
}

print("Welcome! You can look up the birthdays of the people in the list!")
person_add = input("Who would you like to be stored in the dictionary? ____ ")
person_add_birthday = input('What is his(her) birthday? _____ ')
birthdays[person_add] = person_add_birthday

print(f'You can choose from this list of persons:\n', ", ".join(birthdays.keys()))


person_name = input("Whose birthday would you like to know? ____ ")
birthday = birthdays.get(person_name)

# Print out the birthday with a nicely-formatted message
if birthday:
    print(f"The birthday of {person_name} is: {birthday}")
else:
    print(f"Sorry, we don't have the birthday for {person_name}.")

# Exercise 4: Fruit Shop
items = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}
#1
for key, value in items.items():
    print(f"The price for{key} is {value}!")
#2
items = {
    "banana": {"price": 4 , "stock":10},
    "apple": {"price": 2, "stock":5},
    "orange": {"price": 1.5 , "stock":24},
    "pear": {"price": 3 , "stock":1}
}
summ = 0
for key, value in items.items():
    summ += items[key]['price']*items[key]['stock']
print(f'It would cost {summ} summ')
