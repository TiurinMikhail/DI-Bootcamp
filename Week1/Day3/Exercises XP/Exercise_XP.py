#Exercise 1 : Convert Lists Into Dictionaries
keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]
word_to_num = dict(zip(keys,values))
print(word_to_num)

#Exercise 2 : Cinemax
family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}
summ = 0
for key,value in family.items():
    if value >= 3 and value <= 12:
        print(f'{key.capitalize()} nedd to pay {10}')
        summ += 10
    elif value > 12:
        print(f'{key.capitalize()} nedd to pay {15}')
        summ += 15
print(f'Family’s total cost for the movies is {summ}')

#Exercise 3: Zara
brand = {'name': 'Zara',
'creation_date': 1975,
'creator_name': 'Amancio Ortega Gaona',
'type_of_clothes': ['men', 'women', 'children', 'home'],
'international_competitors': ['Gap', 'H&M', 'Benetton'],
'number_stores': 7000,
'major_color':
    {'France': 'blue',
    'Spain': 'red',
    'US': ('pink', 'green')}}
#3
brand['number_stores'] = 2
#4
print(brand['type_of_clothes'][:3])
#5
brand['country_creation'] = 'Spain'
#6
if brand.get('international_competitors') != None:
    brand['international_competitors'].append('Desigual')
#7 If we need to make None in the value. Otherway we need to delete the pair key-value.
brand['creation_date'] = None
print(brand['creation_date'])
del brand['creation_date']

#8
print(brand['international_competitors'][-1])
#9
mj_clr_us = brand['major_color']['US']
print(f'The major clothes colors in the US: {mj_clr_us}',sep='\n')
#or
for item in brand['major_color']['US']:
    print(item)
#10
print(f'Length of the dictionary is: {len(brand)}')
#11
print(f'Keys of the dictionary: {brand.keys()}')
#12
more_on_zara = {'creation_date': 1975,
'number_stores': 10000}
#13
brand.update(more_on_zara)
#14 So, in this two dictionaries we have the same keys- 'number_stores'. when we use update(),
# the function will find this problem and won't add the same key-value pair,
# it will just update the value num.
print(brand['number_stores'])

#Exercise 4 : Disney Characters
users = ["Mickey","Minnie","Donald","Ariel","Pluto"]
disney_users_A = {}
disney_users_B = {}
disney_users_C = {}
#1/ disney_users_A
for i in range(len(users)):
    disney_users_A[users[i]] = i
print(disney_users_A)
#2/ disney_users_B
for i in range(len(users)):
    disney_users_B[i] = users[i]
print(disney_users_B)
#3/ disney_users_B
users_sorted = sorted(users)
for i in range(len(users_sorted)):
    disney_users_C[users_sorted[i]] = i
print(disney_users_C)
#4
disney_users_A_recreated = {}
for key in disney_users_A.keys():
    if (key.lower().startswith('m') or key.lower().startswith('p')) and 'i' in key:
        disney_users_A_recreated.update({key: disney_users_A[key]})
print(disney_users_A_recreated)







