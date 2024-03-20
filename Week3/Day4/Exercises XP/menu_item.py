import psycopg2

HOSTNAME = 'localhost'
USERNAME = 'postgres'
PASSWORD = '2112'
DATABASE = 'restaurant '

class Menu_item:
    def __init__(self, name, price):
        self.name = name
        self.price = price
        # self.connection = psycopg2.connect(host=HOSTNAME, user=USERNAME, password=PASSWORD, dbname=DATABASE)
        # self.cursor = self.connection.cursor()
    def __str__(self):
        return f'{self.name} - {self.price}'

    def save(self):
        try:
            connection = psycopg2.connect(host=HOSTNAME, user=USERNAME, password=PASSWORD, dbname=DATABASE)
            cursor = connection.cursor()
            query = f"insert into Menu_Items(item_name,item_price) values('{self.name}',{self.price});"
            cursor.execute(query)
            connection.commit()
            connection.close()
            print("Item saved successfully!")
        except psycopg2.Error as error:
            print(f"Error while saving item:",error)

    def delete(self):
        try:
            connection = psycopg2.connect(host=HOSTNAME, user=USERNAME, password=PASSWORD, dbname=DATABASE)
            cursor = connection.cursor()
            cursor.execute(f"DELETE from Menu_Items WHERE item_name = '{self.name}';")
            connection.commit()
            cursor.close()
            connection.close()
            print("Item deleted successfully!")
        except psycopg2.Error as e:
            print("Error while deleting item:", e)

    def update(self, item_name=None, item_price= None):
        try:
            connection = psycopg2.connect(host=HOSTNAME, user=USERNAME, password=PASSWORD, dbname=DATABASE)
            cursor = connection.cursor()
            if item_name is not None and item_price is not None:
                update_query = f"UPDATE Menu_Items SET item_name = '{item_name}', item_price = {item_price} WHERE item_name = '{self.name}' and item_price = {self.price};"
                cursor.execute(update_query)
            elif item_name:
                update_query = f"UPDATE Menu_Items SET item_name = '{item_name}' WHERE item_name = '{self.name}' and item_price = {self.price};"
                cursor.execute(update_query)
            elif item_price:
                update_query = f"UPDATE Menu_Items SET item_price = {item_price} WHERE item_name = '{self.name}' and item_price = {self.price};"
                cursor.execute(update_query)
            connection.commit()
            cursor.close()
            connection.close()
            print("Item updated successfully!")
        except psycopg2.Error as e:
            print("Error while updating item:", e)

if __name__ == '__main__':
    item = Menu_item('Burger', 35)
    item.save()
    # # item.delete()
    # item.update('Veggie Burger', 37)


