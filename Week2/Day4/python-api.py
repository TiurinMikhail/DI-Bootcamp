import requests
import json

response = requests.get('https://api.chucknorris.io/jokes/random')

print(response) #<Response= 200- Sucess#  300 = redirect , 400 = error/not available , 404 = not found#

print(response.text)

print(type(response.text))

jokes = []

for i in range(10):
    response = requests.get('https://api.chucknorris.io/jokes/random')
    data = response.json()['value']
    jokes.append(data)

for joke in jokes:
    print(joke)