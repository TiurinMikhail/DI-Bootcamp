from menu_manager import MenuManager
from menu_item import Menu_item
# Part 2

def show_user_menu():
    while True:
        print('     MENU\n', '(V) View an Item\n', '(A) Add an Item\n', '(D) Delete an Item\n', '(U) Update an Item\n', '(S) Show the Menu\n', '(X) Exit the program')
        choice = input('Enter your choice: ').upper()
        if choice == 'V':
            print(MenuManager.get_by_name(input('Enter name of the item in the menu: ')))
        elif choice == 'A':
            add_item_to_menu()
        elif choice == 'D':
            remove_item_from_menu()
        elif choice == 'U':
            update_item_from_menu()
        elif choice == 'S':
            print(MenuManager.all_items())
        elif choice == 'X':
            print(MenuManager.all_items())
            break


def add_item_to_menu():
        name = input('What is the name of adding item?')
        price = int(input('What is the price of adding item?'))
        item = Menu_item(name, price)
        item.save()

def remove_item_from_menu():
    name = input('What is the name of the item to remove?')
    result = MenuManager.get_by_name(name)
    item = Menu_item(result[1],result[2])
    item.delete()

def update_item_from_menu():
    name = input('What is the name of updating item?')
    # price = int(input('What is the price of updating item'))
    result = MenuManager.get_by_name(name)
    item = Menu_item(result[1], result[2])
    new_name = input('What is the new name of updating item?')
    new_price = int(input('What is the new price of updating item?'))
    item.update(new_name, new_price)


def show_restaurant_menu():
    print(MenuManager.all_items())


show_user_menu()


