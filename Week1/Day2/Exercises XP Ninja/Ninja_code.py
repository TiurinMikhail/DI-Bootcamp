#Exercise 1: Formula
#Q = Square root of [(2 * C * D)/H]
C = 50
H = 30
numbers = [int(i) for i in input("Enter numbers separated by commas in one string: ").split(',')]
Q_list = []
for num in numbers:
    D = num
    Q = ((2*C*D)/H)**(0.5)
    Q_list.append(str(int(Q)))
print(','.join(Q_list))

#Exercise 2 : List Of Integers
integers_lists = [
    [3, 47, 99, -80, 22, 97, 54, -23, 5, 7],
    [44, 91, 8, 24, -6, 0, 56, 8, 100, 2],
    [3, 21, 76, 53, 9, -82, -3, 49, 1, 76],
    [18, 19, 2, 56, 33, 17, 41, -63, -82, 1]
]
union_numbers = [num for sublist in integers_lists for num in sublist]
print(union_numbers)
print(sorted(union_numbers)[::-1]) # or print(sorted(union_numbers, reverse=True)
print(sum(union_numbers))
first_last = [i for i in union_numbers if i == union_numbers[0] or i == union_numbers[-1]]
greater_50 = [i for i in union_numbers if i > 50]
smaller_10 = [i for i in union_numbers if i < 10]
integers_list_squared = [i**2 for i in union_numbers]
integers_list_unic = []
for i in union_numbers:
    if i not in integers_list_unic:
        integers_list_unic.append(i)
print(len(union_numbers))
print(sum(union_numbers)/len(union_numbers))
print(max(union_numbers))
print(min(union_numbers))
#11 Bonus
summ = 0
largest = -10**8
smallest = 10**8
cnt_el = 0
for i in union_numbers:
    cnt_el += 1
    summ += i
    if i > largest:
        largest = i
    if i < smallest:
        smallest = i
average = summ/cnt_el
print(largest, smallest, summ, average)
#12 Bonus
user_numbers = []

for _ in range(10):
    while True:
        try:
            number = int(input("Please enter a number between -100 and 100: "))
            if -100 <= number <= 100:
                user_numbers.append(number)
                break
            else:
                print("Number must be between -100 and 100. Try again.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
#13
import random as rd

random_numbers = [rd.randint(-100, 100) for _ in range(10)]
# 14
num_integers = rd.randint(50, 100)

random_numbers2 = [rd.randint(-100, 100) for _ in range(num_integers)]

#15

#Yes, the code will work regardless of the number of random numbers generated.
# The program dynamically determines the number of random numbers to generate based on the
# randomly chosen value between 50 and 100.


#Exercise 3: Working On A Paragraph
text = 'In essence, while other animals are locked into a mode of existence dictated by their genetic code, humans are subject to a second kind of natural selection, which operates on ideas rather than genes. Just as genetic mutations have shaped the evolution of plants and animals, cultural mutations have shaped the evolution of Homo sapiens. The most important difference between us and other animals is the level of our imagination and our ability to cooperate. These abilities have allowed Homo sapiens to spread from its African homeland and become the dominant species across the planet.'
setneces = 0
if text[-1] == '.':
    setneces = len(text.split('.')) - 1
else:
    setneces = len(text.split('.'))
words_cnt = len(text.split())
words_list = []
word = ''
for char in text:
    if char.isalpha():
        word += char.lower()
    else:
        if word != '':
            words_list.append(word)
        word = ''
text_unic_words = []
for word in words_list:
    if word not in text_unic_words:
        text_unic_words.append(word)

print(f'This text contains {len(text)} characters,{setneces} sentences,{words_cnt} words and {len(text_unic_words)} unic words.')
non_spaces = [char for char in text if char != ' ']
print(len(non_spaces))
print(f'The average amount of words per sentence in the paragraph is {avg_amnt_words}')

#Exercise 4
user_input= input('Enter your sentence').split()
for item in user_input:
    print(f'{item}:{user_input.count(item)}')