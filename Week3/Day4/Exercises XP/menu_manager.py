import psycopg2

HOSTNAME = 'localhost'
USERNAME = 'postgres'
PASSWORD = '2112'
DATABASE = 'restaurant '


class MenuManager:
    @classmethod
    def get_by_name(cls, item_name):
        try:
            connection = psycopg2.connect(host=HOSTNAME, user=USERNAME, password=PASSWORD, dbname=DATABASE)
            cursor = connection.cursor()
            select_query = f"SELECT * FROM Menu_Items WHERE item_name = '{item_name}'"
            cursor.execute(select_query)
            item = cursor.fetchone()
            cursor.close()
            connection.close()
            if item:
                return item
            else:
                return None
        except psycopg2.Error as e:
            print("Error while fetching item by name:", e)
            return None

    @classmethod
    def all_items(cls):
        try:
            connection = psycopg2.connect(host=HOSTNAME, user=USERNAME, password=PASSWORD, dbname=DATABASE)
            cursor = connection.cursor()
            select_query = f"SELECT * FROM Menu_Items"
            cursor.execute(select_query)
            items = cursor.fetchall()
            cursor.close()
            connection.close()
            return items
        except psycopg2.Error as e:
            print("Error while fetching all items:", e)
            return None

if __name__ == '__main__':
    print(MenuManager.get_by_name("Veggie Burger"))
    print(MenuManager.all_items())