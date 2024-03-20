import requests
import json
import random
import psycopg2

API_URL = 'https://restcountries.com/v3.1/all'

HOSTNAME = 'localhost'
USERNAME = 'postgres'
PASSWORD = '2112'
DATABASE = 'countries'

response = requests.get(API_URL)

response_json = response.json()
print(response_json)

def get_random_country_to_db():
    random_country = random.sample(response_json,10)
    for country in random_country:
        country_name = country['name']['official'].replace("'", '')
        subregion = country['subregion'].replace("'", '')
        # language = country['languages']['ell']
        flag = country['flags']['png']
        capital = country['capital'][0].replace("'", '')
        population_cntry = country['population']
        connection = psycopg2.connect(host=HOSTNAME, user=USERNAME, password=PASSWORD, dbname=DATABASE)
        cursor = connection.cursor()
        query = f"""INSERT INTO countries(country_name, capital_name, flag, subregion, population) VALUES ('{country_name}','{capital}','{flag}','{subregion}',{population_cntry});"""
        cursor.execute(query)
        connection.commit()
        connection.close()


get_random_country_to_db()