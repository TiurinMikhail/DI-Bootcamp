print('----------')
# Read the file line by line
with open(dir_path + '/nameslist.txt', 'r') as file_obj:
    content = file_obj.read()
    print(content)
print('-----------')
# Read only the 5th line of the file
with open(dir_path + '/nameslist.txt', 'r') as file_obj:
    content = file_obj.readlines()
    print(content[4])
print('-------')
# Read only the 5 first characters of the file
with open(dir_path + '/nameslist.txt', 'r') as file_obj:
    content = file_obj.read(5)
    print(content)

print('-----------')
# Read all the file and return it as a list of strings. Then split each word
with open(dir_path + '/nameslist.txt', 'r') as file_obj:
    content_list = file_obj.readlines()
    for content in content_list:
        if '\n' in content:
            content = content[:-1]
        print(list(content))

# Find out how many occurences of the names "Darth", "Luke" and "Lea" are in the file
with open(dir_path + '/nameslist.txt', 'r') as file_obj:
    content_list = file_obj.readlines()
    dict_names = {}
    counter_d = 0
    counter_Luke = 0
    counter_Lea = 0
    for content in content_list:
        content = ''.join(content.split())
        if content == 'Darth':
            counter_d += 1
        elif content == 'Luke':
            counter_Luke += 1
        elif content == 'Lea':
            counter_Lea += 1
    dict_names['Darth'] = counter_d
    dict_names['Luke'] = counter_Luke
    dict_names['Lea'] = counter_Lea
    print(dict_names)

#
with open(dir_path + '/nameslist.txt', 'a') as file_obj:
    content = file_obj.write('\nMichael')

# Append "SkyWalker" next to each first name "Luke"
with open(dir_path + '/nameslist.txt', 'a+') as file_obj:
    content_list = file_obj.readlines()
    for content in content_list:
        if content[:-1] == 'Luke':
            pass
