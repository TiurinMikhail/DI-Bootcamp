#Exercise 1 : Set
my_fav_numbers = set([2,3,5,7,8,10,12,17,21,25])
my_fav_numbers.update([27,30])
#Remove the last number --- We can do it only if we know the value of rhe "last" item, because set does not have indexes
# For ex:my_fav_numbers.remove(30)

friend_fav_numbers = set([3, 11, 18])
# Concatenate my_fav_numbers and friend_fav_numbers to a new variable called our_fav_numbers
our_fav_numbers = my_fav_numbers|friend_fav_numbers
print(our_fav_numbers)


#Exercise 2: Tuple
#Directly no, but you make use list function to add new int and then formate it back to tuple()

#Exercise 3: List
basket = ["Banana", "Apples", "Oranges", "Blueberries"]
basket.remove("Banana")
basket.remove("Blueberries")
basket.append("Kiwi")
basket.insert(0,"Apples")
print(basket.count("Apples"))
basket.clear()
print(basket)

#Exercise 4: Floats
#A float, short for "floating-point number," is a data type used in python to represent
# decimal numbers. Unlike integers, which represent whole numbers without a fractional part,
# floats can represent numbers with decimal points

#creating a list of floats
num = 1.5
floats_list=[]
for i in range(8):
    floats_list.append(num)
    num+=0.5
print(floats_list)

#or using list comprehensions
floats_list = [i/2 for i in range(3,11)]

#Exercise 5: For Loop
for i in range(1,21):
    print(i)
print()
for i in range(1,21):
    if i % 2 == 0:
        print(i)

#Exercise 6 : While Loop
my_name = 'mikhail'
while True:
    user_name = input('Enter your name: ').lower()
    if my_name == user_name:
        break

#Exercise 7: Favorite Fruits
user_fruits = input('Please,input their favorite fruit(s) (one or several fruits). Separate the fruits with a single space: ').lower().split()
user_choice_fruit = input('Please input a name of any fruit: ').lower()
if user_choice_fruit in user_fruits:
    print('You chose one of your favorite fruits! Enjoy!')
else:
    print('You chose a new fruit. I hope you enjoy')

#Exercise 8: Who Ordered A Pizza ?
pizza_toppings = []
while True:
    user_input = input('Please enter pizza topping here (enter "quit" when you finish): ').lower()
    if user_input != 'quit':
        pizza_toppings.append(user_input)
        print(f'I added {user_input} topping to their pizza')
    else:
        break
total_price = 10+len(pizza_toppings)*2.5
print(f'Your toppings: ', *pizza_toppings, f'Total price is {total_price}', sep='\n')

#Exercise 9: Cinemax
family_size = input('Please enter how many people in your family? ')
family_size = int(family_size)
family_ages = []
for i in range(family_size):
    age = int(input('Please enter the age of the first member of your family (enter ages one by one).'))
    family_ages.append(age)
total_coast = 0
for age in family_ages:
    if 3 <= age <= 12:
        total_coast += 10
    elif age > 12:
        total_coast += 15
print(total_coast)

#teenager
teenager_names = ['Andrew', 'Joseph', 'Daniel', 'Roni','Marcel','Moshe','Kanan','Mikhail']
tenn_restr = []
for item in teenager_names:
    age = int(input(f'Enter your age,{item}: '))
    if age <= 21:
        tenn_restr.append(item)
for item in tenn_restr:
    teenager_names.remove(item)
print(teenager_names)

#Exercise 10 : Sandwich Orders
sandwich_orders = ["Tuna sandwich", "Pastrami sandwich", "Avocado sandwich", "Pastrami sandwich", "Egg sandwich", "Chicken sandwich", "Pastrami sandwich"]
while "Pastrami sandwich" in sandwich_orders:
    sandwich_orders.remove("Pastrami sandwich")
print(sandwich_orders)

finished_sandwiches = []
while sandwich_orders != []:
    finished_sandwiches.append(sandwich_orders[0])
    sandwich_orders.remove(sandwich_orders[0])
for item in finished_sandwiches:
    print(f'I made your {item}.')