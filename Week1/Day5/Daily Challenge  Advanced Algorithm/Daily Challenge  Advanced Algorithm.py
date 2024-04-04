#Daily Challenge  Advanced Algorithm
import random

list_of_numbers = [random.randint(0, 10) for _ in range(1000)]
target_number = 4

def sum_couples(list_of_numbers, target_number):
    unic_pair = {}
    pairs_counter = 0
    list_off_pairs = []
    # make a dict with unic numbers as a key and the number of it in the list as a value
    for number in list_of_numbers:
        if number in unic_pair:
            unic_pair[number] += 1
        else:
            unic_pair[number] = 1
    for number in list_of_numbers:
        complement = target_number - number
        # if it is in dict
        if complement in unic_pair:
            pairs_counter += unic_pair[complement]
            list_off_pairs.append((complement, number))
        # do not count the same pair twice
        if complement == number:
            pairs_counter -= 1
    print(len(set(list_off_pairs)))
    print(len(list_off_pairs))
    return pairs_counter//2

n = sum_couples(list_of_numbers,target_number)

print(f'The number of pairs is {n}')



