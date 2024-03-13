import requests
import json

#Exercise 3 : Giphy API #2
term = input('Enter the term: ')
url = f'https://api.giphy.com/v1/gifs/search?q={term}&rating=g&api_key=hpvZycW22qCjn5cRM1xtWB8NKq4dQ2My'
response3 = requests.get(url)
if response3.status_code == 200:
    data = response3.json()
    print(len(data['data']))
