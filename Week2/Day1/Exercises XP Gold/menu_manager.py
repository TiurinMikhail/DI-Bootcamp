#Exercise 3 : Restaurant Menu Manager

class MenuManager:
    def __init__(self, menu):
        self.menu = menu

    def print_menu(self):
        print(self.menu)

    def add_item(self, name, price, spice, gluten):
        self.menu.append({'name': name, 'price': price, 'spice': spice, 'gluten': gluten})

    def update_item(self, name, price, spice, gluten):
        flag = False
        for dic in self.menu:
            if dic['name'] == name:
                dic.update({'name': name, 'price': price, 'spice': spice, 'gluten': gluten})
                flag = True
        if not flag:
            print('Item is not found!')

    def remove_item(self,name):
        for dic in self.menu:
            if dic['name'] == name:
                self.menu.remove(dic)

menu = MenuManager([{'name': 'Sibas', 'price': 10, 'spice': 'C', 'gluten': False},{'name': 'Beef', 'price': 14, 'spice': 'A', 'gluten': False}])

menu.add_item('Pork',8,'B',False)
menu.add_item('Potato',4,'A',True)
menu.print_menu()

menu.update_item('Pork',10,'C',False)
menu.print_menu()

menu.remove_item('Pork')
menu.print_menu()
menu.update_item('Batat',4,'A',True)
