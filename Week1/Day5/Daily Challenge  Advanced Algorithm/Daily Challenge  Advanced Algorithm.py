#Daily Challenge  Advanced Algorithm
import random

list_of_numbers = [random.randint(0, 10000) for _ in range(20000)]
target_number = 3728

def sum_couples(list_of_numbers, target_number):
    cnt = 0
    flag = False
    for i in range(0,len(list_of_numbers)-1):
        if list_of_numbers[i] + list_of_numbers[i+1] == target_number:
            cnt += 1
            flag = True
    if flag == False:
        print('No solution at this generating')
    else:
        print(f'There are {cnt} solutions at this generating')
sum_couples(list_of_numbers, 3728)
