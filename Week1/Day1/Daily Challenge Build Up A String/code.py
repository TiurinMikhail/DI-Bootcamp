user_string = input("Enter a string: ")
if len(user_string) < 10:
    print('string not long enough')
elif len(user_string) > 10:
    print('string too long')
else:
    print('perfect string')

print(user_string[0],user_string[-1],sep='\n')

print()

string_out = ''
for i in range(len(user_string)):
    string_out += user_string[i]
    print(string_out)

#or
ind = 1
for i in range(len(user_string)):
    print(user_string[:ind])
    ind += 1


import random as rd

chars = list(user_string)
rd.shuffle(chars)
user_string_new = ''.join(chars)
print(user_string_new)
