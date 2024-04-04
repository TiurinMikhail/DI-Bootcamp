#Challenge 1
number = int(input("Enter your number: "))
length = int(input('Enter the length of the creating list: '))
multiples_list = []
for i in range(1,length+1):
    multiples_list.append(number*i)
print(multiples_list)

#Challenge 2
user_string = input("Enter your word: ")
final_string = ''
for i in range(len(user_string)):
    if user_string[i] != user_string[i-1] or i ==0:
        final_string += user_string[i]
print(final_string)
#or!!