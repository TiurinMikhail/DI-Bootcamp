#Exercise 1 : Hello World
print('Hello world\n'*4)

#Exercise 2 : Some Math
print((99**3)*8)


# Exercise 3 : What Is The Output ?
#print(5 < 3) # False
#print(3 == 3) #True
#print(3 == "3") # False
#print("3" > 3) # TypeError
#print("Hello" == "hello") # False

#Exercise 4 : Your Computer Brand
computer_brand = 'Redmi'
print(f'I have a {computer_brand} computer')

#Exercise 5 : Your Information
name = 'Mikhail'
age = 24
shoe_size = 43
info = f'My name is {name}. I am {age} years old. The size of my shoe is {shoe_size}.'
print(info)
#Exercise 6 : A & B
a = 4
b = 5
if a > b:
    print('Hello World')
#Exercise 7 : Odd Or Even
number = int(input('Give me a number: '))
if number%2 == 0:
    print('Even number')
else:
    print('Odd number')
#Exercise 8 : What’s Your Name ?
user_name = input('What’s Your Name?: ').lower()
if user_name == 'mikhail' or user_name == 'michael':
    print('You do not say! It is impossible!!!')
#Exercise 9 : Tall Enough To Ride A Roller Coaster
user_height = int(input('What is your height(in inches): '))
user_height_cm = user_height*2.54
if user_height_cm > 145:
    print('You are tall enough to ride')
else:
    print('You need to grow some more to ride')
