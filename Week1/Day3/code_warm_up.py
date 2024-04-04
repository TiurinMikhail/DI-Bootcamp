names = ['name1', 'name2', 'name3']
grades = [90, 80, 70]
grades_dict = {key:value+10 for key,value in zip(names,grades)}
print(grades_dict)

def find_in_dict(input_dict,value):
    keys =[]
    for key, cur_value in input_dict.items():
        if cur_value == value:
            keys.append(key)
    return keys

print(find_in_dict(grades_dict,90))

def delete_zeros(in_list):
    without_zeros = []
    for i,value in enumerate(in_list):
        if value != 0:
            without_zeros.append(value)
    return without_zeros

list1 = [0,1,0,2,0,3,0,4]


#Write a function calculation() such that it can accept two variables and calculate the
# addition and subtraction of it. And also it must return both addition and subtraction in a
# single return call

def calculation(num1,num2):
    return num1+num2,num1/num2
calculation(2,3)

some_lists = ['a','b','c','b','d','m','n','n']

duplicates = list(set([i for i in some_lists if some_lists.count(i) > 1 ]))
print(duplicates)

a = ["b", "g", "a", "d", "f", "c", "h", "e"]
x = sorted(a)
print("a after sorted function")
print(a)
print(x)
b = [1, 2, 5, 8, 3]
b.sort()
print(b)

# Exercise 4 : Random
import random as rd


def compare_rd_numbers(number):
    rd_number = rd.randint(1,100)
    if rd_number == number:
        print('Success!')
    else:
        print('Fail!',number,rd_number)

