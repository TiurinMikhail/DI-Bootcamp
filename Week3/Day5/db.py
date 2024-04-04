# import psycopg2
#
# conn = psycopg2.connect('postgres://ljegpnle:s52KtrB_NVDjrDKJM4qPGF8T1nSSkERE@flora.db.elephantsql.com/ljegpnle')
#
# cur = conn.cursor()
#
# cur.execute("SELECT * FROM public.harmful_resources")
#
# # Fetch all the results
# result = cur.fetchall()
#
# # Print the results
# for row in result:
#     print(row)
#
# # Close the cursor and connection
# cur.close()
# conn.close()
#
# def insert_resource(resource_name, resource_url, harmful_score):
#     try:
#         cur.execute(
#             "INSERT INTO harmful_resources (resource_name, resource_url, harmful_score) VALUES (%s, %s, %s)",
#             (resource_name, resource_url, harmful_score)
#         )
#         conn.commit()
#         print("Data inserted successfully!")
#     except psycopg2.Error as e:
#         conn.rollback()
#         print("Error inserting data:", e)
#
# def delete_resource(resource_id):
#     try:
#         cur.execute(
#             "DELETE FROM harmful_resources WHERE resource_id = %s",
#             (resource_id,)
#         )
#         conn.commit()
#         print("Row deleted successfully!")
#     except psycopg2.Error as e:
#         conn.rollback()
#         print("Error deleting row:", e)
#
# # # Example usage
# # # Inserting data into the table
# # insert_resource("Malicious Website", "http://example.com/malicious", 9)
# #
# # # Deleting a row from the table
# # delete_resource(1)
# #
# # # Close the cursor and connection
# # cur.close()
# # conn.close()
from selenium import webdriver
from bs4 import BeautifulSoup

# Укажите полный путь к файлу chromedriver.exe
chrome_driver_path = 'C:/Users/v_gol/Downloads/chromedriver_win32/chromedriver.exe'

# URL страницы для скрапинга
url = 'https://apnews.com/hub/anti-semitism'

# Используем Selenium для загрузки страницы
driver = webdriver.Chrome(executable_path=chrome_driver_path)

# Получаем HTML содержимое страницы после загрузки JavaScript
driver.get(url)
html_content = driver.page_source

# Создаем объект BeautifulSoup для парсинга HTML
soup = BeautifulSoup(html_content, 'html.parser')

# Находим все элементы с классом "view-content"
view_content = soup.find_all(class_='view-content')

if not view_content:
    print("No view-content elements found on the page.")
else:
    print(f"Found {len(view_content)} view-content elements.")

    # Проходимся по каждому элементу и извлекаем информацию
    for content in view_content:
        # Находим все элементы с классом "views-row"
        views_rows = content.find_all(class_='views-row')
        for row in views_rows:
            # Находим заголовок и ссылку
            title_element = row.find(class_='small-card__title').find('a')
            title = title_element.text.strip()
            href = title_element['href']

            # Находим дату
            date = row.find(class_='small-card__date').text.strip()

            # Выводим информацию
            print("Title:", title)
            print("Link:", href)
            print("Date:", date)
            print()

# Закрываем браузер после использования
driver.quit()