#Challenge 1
user_word = input('Enter a word: ')
index_dict = {key:[] for key in user_word}

for key in index_dict.keys():
    for i in range(len(user_word)):
        if user_word[i] == key:
            index_dict[key].append(i)
print(index_dict)

# Challenge 2
items_purchase = {
  "Water": "$1",
  "Bread": "$3",
  "TV": "$1,000",
  "Fertilizer": "$20"
}

wallet = "$300"
wallet = int(wallet[1:])
for key,value in items_purchase.items():
    if '$' in value or ',' in value:
        items_purchase[key] = value.replace('$','').replace(',','')
list_of_store = []
summ = 0
for key,value in items_purchase.items():
    if int(value) < wallet:
        summ += int(value)
        if summ < wallet:
            list_of_store.append(key)
if list_of_store == []:
    print('Nothing')
else:
    print(list_of_store)


items_purchase = {
  "Apple": "$4",
  "Honey": "$3",
  "Fan": "$14",
  "Bananas": "$4",
  "Pan": "$100",
  "Spoon": "$2"
}

wallet = "$100"

wallet = int(wallet[1:])
for key,value in items_purchase.items():
    if '$' in value or ',' in value:
        items_purchase[key] = value.replace('$','').replace(',','')
list_of_store = []
summ = 0
for key,value in items_purchase.items():
    if int(value) < wallet:
        summ += int(value)
        if summ < wallet:
            list_of_store.append(key)
if list_of_store == []:
    print('Nothing')
else:
    print(list_of_store)

items_purchase = {
  "Phone": "$999",
  "Speakers": "$300",
  "Laptop": "$5,000",
  "PC": "$1200"
}

wallet = "$1"

wallet = int(wallet[1:])
for key,value in items_purchase.items():
    if '$' in value or ',' in value:
        items_purchase[key] = value.replace('$','').replace(',','')
list_of_store = []
summ = 0
for key,value in items_purchase.items():
    if int(value) < wallet:
        summ += int(value)
        if summ < wallet:
            list_of_store.append(key)
if list_of_store == []:
    print('Nothing')
else:
    print(list_of_store)
