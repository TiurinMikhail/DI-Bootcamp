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

def divide_list(list_to_divide):
    integer_list = []
    string_list = []
    for element in list_to_divide:
        if type(element) == int:
            integer_list.append(element)
        elif type(element) == str:
            string_list.append(element)
    return integer_list, string_list

integer_list,string_list = divide_list([1,2,3,4,5,'dsfsd','adsfasdf','asdfas',23])
print(integer_list)
print(string_list)

#Exercise 12 - Write a function to check if a string is a palindrome:
def is_palindrom(word):
    if word[:] == word[::-1]:
        print('YES')
    else:
        print('NO')

def is_palindrom_v2(word):
    if word[:] == word[::-1]:
        return True
    else:
        return False


is_palindrom('radar')
is_palindrom('John')
print(is_palindrom_v2('radar'))
print(is_palindrom_v2('John'))

#Exercise 13 - Write a function that returns the amount of words in a sentence with length > k:
def length_over_k(sentence,k):
    sum_over_k = 0
    sentence = sentence.replace('.', '').replace(',', '').replace('?', '').replace('!', '').replace(':', '')
    sentence = sentence.split()
    for word in sentence:
        if len(word) > k:
            sum_over_k += 1
    return sum_over_k

print(length_over_k('Do or do not there is no try',2))

#Exercise 14 - Write a function that returns the average value in a dictionary (assume the values are numeric):
def dict_avg(dictionary):
    return (sum(dictionary.values())/len(dictionary))

print(dict_avg({'a': 1,'b':2,'c':8,'d': 1}))

#Exercise 15 - Write a function that returns common divisors of 2 numbers:
def common_div(num1,num2):
    common_div_list = []
    if num1 < num2:
        for number in range(1,num2+1): # here we can start from 2, but I suppose, that 1 must be included
            if num1 % number == 0 and num2 % number == 0:
                common_div_list.append(number)
    return common_div_list

common_list = common_div(10,20)
print(common_list)


#Exercise 16 - Write a function that test if a number is prime:
def is_prime_number(number):
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

print(is_prime_number(11))

#Exercise 17 - Write a function that prints elements of a list if the index and the value are even:
def weird_print(list_to_check):
    weird_list = []
    for i in range(len(list_to_check)):
        if list_to_check[i] % 2 == 0 and i % 2 == 0:
            weird_list.append(list_to_check[i])
    print(weird_list)

weird_print([1,2,2,3,4,5])

#Exercise 18 - Write a function that accepts an undefined number of keyworded arguments and return the count of different types:
def type_count(**args):
    integer_count = 0
    string_count = 0
    float_count = 0
    bool_count = 0
    for value in args.values():
        if type(value) == int:
            integer_count += 1
        elif type(value) == float:
            float_count += 1
        elif type(value) == bool:
            bool_count += 1
        elif type(value) == str:
            string_count += 1
    print(f'int:{integer_count}, string:{string_count}, float:{float_count}, bool:{bool_count}')

type_count(a=1,b='string',c=1.0,d=True,e=False)

# Exercise 19 - Write a function that mimics the builtin .split() method for strings.
# By default the function uses whitespace but it should be able to take an argument for any character and split with that argument.

def mimic_split(string,separator):
    split_string = []
    cnt = 0
    for i in range(len(string)):
        if string[i] == separator:
            split_string.append(string[cnt:i])
            cnt = i
    split_string.append(string[cnt+1:])
    return split_string

split_string = mimic_split('To do or not to do',',')
print(split_string)


#Exercise 20 - Convert a string into password format.
# Example:
# input : "mypassword"
# output: "***********"

def convert_password(password):
    print("*"*len(password))

convert_password('PASSWORD')