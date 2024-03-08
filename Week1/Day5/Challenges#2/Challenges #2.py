#Challenges #2
#Exercise 1
#Instructions
#Draw the following pattern using for loops
n = 3
for i in range(n):
    spaces = n-i-1
    stars = 2*i +1
    print(spaces*' ',stars*'*')

print()

n = 5
for i in range(n):
    spaces = n-i-1
    stars = i+1
    print(spaces * ' ', stars * '*')

print()
for j in range(2):
    for i in range(5):
        if j != 1:
            spaces = n-i-1
            stars = i+1
            print(stars*'*',spaces*' ')
        else:
            print(spaces*' ',stars*'*')
            spaces += 1
            stars -= 1


#Exercise 2
#Instructions
#Analyse this code before executing it. Write some commnts next to each line.
# Write the value of each variable and their changes, and add the final output.\
# Try to understand the purpose of this program.

my_list = [2, 24, 12, 354, 233]
for i in range(len(my_list) - 1): # for numbers [2,24,12,354]
    minimum = i # make a minimum for numbers > 0
    for j in range( i + 1, len(my_list)): # for numbers [24,12,354,233]
        if(my_list[j] < my_list[minimum]): # we check if the first letter is minimum of this list
            minimum = j # if it is not - we make a new minimum
            if(minimum != i): # check for the same number
                my_list[i], my_list[minimum] = my_list[minimum], my_list[i] # change the position of numbers to start from the minimum
print(my_list) # it will print a sorted list of numbers (from min to max)
