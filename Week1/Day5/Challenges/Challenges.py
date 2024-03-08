#Challenges
#Exercise 1 - Write a script that inserts an item at a defined index in a list.

def insert_item(user_list, index, item):
    user_list.insert(index, item)

user_list = [[1,2,3,4,5], 'besseder', 3]

insert_item(user_list, 0, 'sababa')

print(user_list)

#Exercise 2 - Write a script that counts the number of spaces in a string.

def count_spaces(user_string):
    spaces = user_string.count(' ')
    return print(f'The number of spaces: {spaces}')

count_spaces("I love python!")

#Exercise 3 -- Write a script that calculates the number of upper case letters and lower case letters in a string.

def upper_lower_cases(user_string):
    cnt_upper = 0
    cnt_lower = 0
    for letter in user_string:
        if letter.isupper():
            cnt_upper += 1
        elif letter.islower():
            cnt_lower += 1
    return print(f'The number of upper case letters:{cnt_upper}, the number of lower case letters {cnt_lower}')

upper_lower_cases("I love python!I love coding!")

#Exercise 4 - Write a function to find the sum of an array without using the built in function:

def array_sum(user_array):
    summ = 0
    for num in user_array:
        summ += num
    return(summ)

print(array_sum([1,2,3]))

#Exercise 5 -Write a function to find the max number in a list

def max_number(user_array):
    max_number = -10**12
    for num in user_array:
        if num > max_number:
            max_number = num
    return print(f'The maximum number is {max_number}')

user_array = [1,2,3,4,5]
max_number(user_array)


#Exercise 6 -Write a function that returns factorial of a number
def factorial(number):
    factorial = 1
    for i in range(1,number+1):
        factorial *= i
    return print(f'The factorial of {number} is {factorial}')

factorial(4)

#Exercise 7 - Write a function that counts an element in a list (without using the count method)

def count_elements(user_array):
    elements = 0
    for element in user_array:
        elements += 1
    return print(f'{elements} elements in the array')

user_array = [1,2,3,[1,2,3],'asd','asdas','faaf']
count_elements(user_array)


# Exercise 8 - Write a function that returns the L2-norm (square root of the sum of squares) of the sum of a list:

def l2_norm(user_array):
    sum_of_squares = 0
    for num in user_array:
        sum_of_squares += num**2
    return print(f'The l2_norm of the array: {int(sum_of_squares**0.5)}')

user_array = [1,2,2]

l2_norm(user_array)

#Exercise 9 - Write a function to find if an array is monotonic (sorted either ascending of descending)

def is_mono(user_array):
    if user_array == sorted(user_array):
        return True
    elif user_array == sorted(user_array, reverse=True):
        return True
    return False

print(is_mono([7,6,5,5,2,0]))

print(is_mono([2,3,3,3]))

print(is_mono([1,2,0,4]))



#Exercise 10- Write a function that prints the longest word in a list.

def longest_word(user_array):
    longest_word = ''
    for word in user_array:
        if len(word) > len(longest_word):
            longest_word = word
    return longest_word

print(longest_word(['hello','world','python','education','dady','mother']))



# Exercise 11 -Given a list of integers and strings, put all the integers in one list, and all the strings in another one.




#Exercise 12 - Write a function to check if a string is a palindrome:


#Exercise 13 - Write a function that returns the amount of words in a sentence with length > k:

#Exercise 14 - Write a function that returns the average value in a dictionary (assume the values are numeric):


#Exercise 15 - Write a function that returns common divisors of 2 numbers:

#Exercise 16 - Write a function that test if a number is prime:

#Exercise 17 - Write a function that prints elements of a list if the index and the value are even:


#Exercise 18 - Write a function that accepts an undefined number of keyworded arguments and return the count of different types:


# Exercise 19 - Write a function that mimics the builtin .split() method for strings.
# By default the function uses whitespace but it should be able to take an argument for any character and split with that argument.


#Exercise 20 - Convert a string into password format.
# Example:
# input : "mypassword"
# output: "***********"
