import os
import json

dir_path = os.path.dirname(os.path.realpath(__file__))

# Exercise 1 : Restaurant Menu Manager

class MenuManager:
    def __init__(self):
        with open(dir_path + '/package.json', 'r') as f:
            text = f.readlines()
            text = ' '.join(text)
        self.menu = json.loads(text)

    def __str__(self):
        string = ''
        print('Menu:')
        for dictionary in self.menu['items']:
            for key, value in dictionary.items():
                string += f'{key}: {value}\n'
            string += '------------\n'
        return string

    def add_item(self, name, price):
        self.menu['items'].append({'name': name, 'price': price})

    def remove_item(self, name):
        flag = False
        for dictionary in self.menu['items']:
            if dictionary['name'] == name:
                self.menu['items'].remove(dictionary)
                flag = True
        return flag

    def save_to_file(self):
        with open(dir_path+'/package.json', 'w') as f:
            json.dump(self.menu, f, indent=2, sort_keys=True)

#
# menu = MenuManager()
# print(menu)
# menu.add_item('Crocodile',45)
# print(menu)
# menu.remove_item('Crocodile')
# print(menu)
# menu.add_item('Crocodile',45)
# menu.save_to_file()