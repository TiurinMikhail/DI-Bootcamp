#Daily Challenge  Advanced Algorithm
import random

list_of_numbers = [random.randint(0, 10000) for _ in range(20000)]
target_number = 3728
unic_pair = set()

def sum_couples(list_of_numbers, target_number):
    flag = False
    for number in range(len(list_of_numbers)):
        for i in range(len(list_of_numbers)):
            if number + list_of_numbers[i] == target_number and i != number:
                unic_pair.add(number)
                unic_pair.add(list_of_numbers[i])
                flag = True
    if flag == False:
        print('No solution at this generating')
    else:
        print(f'There are {len(unic_pair)} solutions at this generating')
sum_couples(list_of_numbers, 3728)



