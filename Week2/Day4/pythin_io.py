import os

dir_path = os.path.dirname(os.path.realpath(__file__))

#file objects
#
# #old school way: problem is that we can forget to close the file using special command close()!!
# print('This is old school way!\n','-----------\n')
#
# file_obj = open('test.txt')
# content = file_obj.read()
# print(content)
# file_obj.close()
#
# print('---------------')
#
# file_obj = open('C:/Users/v_gol/Desktop/Developers Institute/GitHub/DI-Bootcamp/Week2/Day4/test.txt')
# content = file_obj.read()
# print(content)
# file_obj.close()
#
#
# # create a new file using w+
# file_obj = open('C:/Users/v_gol/Desktop/Developers Institute/GitHub/DI-Bootcamp/Week2/Day4/test2.txt', 'w+')
# file_obj.write('Hello there, added!')
# file_obj.close()
#
# # adding new string to the text file
# file_obj = open('C:/Users/v_gol/Desktop/Developers Institute/GitHub/DI-Bootcamp/Week2/Day4/test.txt', 'a')
# file_obj.write('\nHello there')
# file_obj.close()

#Best practise: use context meneger 'with'

# with open('C:/Users/v_gol/Desktop/Developers Institute/GitHub/DI-Bootcamp/Week2/Day4/test2.txt', 'w+') as file_obj2:
#     file_obj2.write('\nanother thing or example')
#     file_obj2.seek(0) # taking the cursor to the first line
#     content = file_obj2.read() # return a string
#     print(content)
#
# with open(dir_path+'/test.txt', 'r') as file_obj:
#     content = file_obj.readline()
#     print(content,end='')

## reaading methods

# with open(dir_path+'/test.txt', 'r') as file_obj:
#     content1 = file_obj.read(20)
#     content2 = file_obj.readline() #returns a string
#     file_obj.seek(0)
#     content_list = file_obj.readlines() #return a list
#     print(content2, content_list, end='')
#     print(content1, end='')
#
print('----------')
# Read the file line by line
with open(dir_path+'/nameslist.txt', 'r') as file_obj:
      content = file_obj.read()
      print(content)
print('-----------')
#Read only the 5th line of the file
with open(dir_path + '/nameslist.txt', 'r') as file_obj:
    content = file_obj.readlines()
    print(content[4])
print('-------')
#Read only the 5 first characters of the file
with open(dir_path + '/nameslist.txt', 'r') as file_obj:
    content = file_obj.read(5)
    print(content)

print('-----------')
#Read all the file and return it as a list of strings. Then split each word
with open(dir_path + '/nameslist.txt', 'r') as file_obj:
    content_list = file_obj.readlines()
    for content in content_list:
        if '\n' in content:
            content = content[:-1]
        print(list(content))

#Find out how many occurences of the names "Darth", "Luke" and "Lea" are in the file
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
with open(dir_path+'/nameslist.txt', 'a') as file_obj:
    content = file_obj.write('\nMichael')

# Append "SkyWalker" next to each first name "Luke"
with open(dir_path+'/nameslist.txt', 'a+') as file_obj:
    content_list = file_obj.readlines()
    for content in content_list:
        if content[:-1] == 'Luke':
            pass







