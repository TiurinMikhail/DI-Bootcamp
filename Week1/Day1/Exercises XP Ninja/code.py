#You can call python3 from any directory because it's typically installed as a
# system-wide executable. This means that the operating system knows where to find the
# python3 executable regardless of your current directory.






#Exercise 3 : Outputs
#>>> 3 <= 3 < 9 -- True
#>>> 3 == 3 == 3 -- True
#>> bool(0) -- False
#>>> bool(5 == "5") -- False
#>>> bool(4 == 4) == bool("4" == "4") -- True
#>>> bool(bool(None)) -- False

#x = (1 == True)
#y = (1 == False)
#a = True + 4
#b = False + 10

#print("x is", x) -- x is True
#print("y is", y) -- False
#print("a:", a) -- a: 5
#print("b:", b) -- 10

#Exercise 4 : How Many Characters In A Sentence ?
my_text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
print(len(my_text)) # including spaces

#Exercise 5: Longest Word Without A Specific Character
char = 'a'
sp = [0]
while char == char:
    user_input = input('Please, input the longest sentence you can without the character “A”: ').lower()
    if char not in user_input and len(user_input)> max(sp):
        print('You are awesome!')
    sp.append(len(user_input))



