from MenuManager import MenuManager

def load_manager():
    return MenuManager()

def show_user_menu():
    while True:
        print('     MENU\n', '(a) Add an item\n', '(d) Delete an item\n', '(v) View the menu\n', '(x) Exit')
        choice = input('Enter your choice: ')
        if choice == 'a':
            add_item_to_menu()
        elif choice == 'd':
            remove_item_from_menu()
        elif choice == 'v':
            show_restaurant_menu()
        elif choice == 'x':
            menu.save_to_file()
            break

def add_item_to_menu():
    while True:
        try:
            new_item = input('Enter new item name: ')
            item_price = float(input('Enter new item price: '))
            menu.add_item(new_item, item_price)
            print('Item was added successfully.')
            break
        except ValueError:
            print('Invalid input. Please enter a valid item price.')

def remove_item_from_menu():
    while True:
        item_to_remove = input('Enter the item name which you want to remove: ')
        flag = menu.remove_item(item_to_remove)
        if flag:
            print('Item was removed successfully.')
            break
        else:
            print('Error: there is no such item in menu!')


def show_restaurant_menu():
    print(menu)



menu = load_manager()
show_user_menu()
