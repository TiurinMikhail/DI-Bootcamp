# Exercise 2

def parse_price(price):
    return int(price.replace('$', '').replace(',', ''))


def get_affordable_items(items_purchase, wallet):
    affordable_items = []
    balance = parse_price(wallet)
    for product_name, product_price in items_purchase.items():
        cost = parse_price(product_price)
        if balance > cost:
            affordable_items.append(product_name)
            balance = balance - cost

    affordable_items.sort()
    return affordable_items


def print_items(items):
    if items != []:
        print(items)
    else:
        print('Nothing')

stores = []
stores.append(get_affordable_items(items_purchase={
    'Water': '$1',
    'Bread': '$3',
    'TV': '$1,000',
    'Fertilizer': '$20'
}, wallet='$300'))

stores.append(get_affordable_items(items_purchase={
    'Apple': '$4',
    'Honey': '$3',
    'Fan': '$14',
    'Bananas': '$4',
    'Pan': '$100',
    'Spoon': '$2'
}, wallet='$100'))

stores.append(get_affordable_items(items_purchase={
    'Phone': '$999',
    'Speakers': '$300',
    'Laptop': '$5,000',
    'PC': '$1200'
}, wallet='$1'))

for items in stores:
    print_items(items)