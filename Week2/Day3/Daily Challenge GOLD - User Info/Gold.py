#v1
list_of_users = [tuple(input('Enter your name, age and score: ').split(',')) for _ in range(5)]
list_of_users_sorted = sorted(list_of_users, key=lambda x:(x[0],x[1],x[2]))
print(list_of_users_sorted)


#v2
list_of_users = []

# Ask for input 5 times
for _ in range(5):
    name = input("Enter name: ")
    age = input("Enter age: ")
    score = input("Enter score: ")
    list_of_users.append((name, int(age), int(score)))

sorted_users = sorted(list_of_users, key=lambda x: (x[0], x[1], x[2]))

print(sorted_users)
