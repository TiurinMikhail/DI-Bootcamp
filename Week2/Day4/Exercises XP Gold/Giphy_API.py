import requests
import json

url = 'https://api.giphy.com/v1/gifs/search?q=hilarious&rating=g&api_key=hpvZycW22qCjn5cRM1xtWB8NKq4dQ2My'
requests.get(url)

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print(len(data['data']))
    print(data)
    # Use f-strings and variables to build the URL string we’re using for the fetch.
    url_first_part = 'https://api.giphy.com/v1/gifs/search?'
    q = 'q=hilarious&'
    rating = 'rating=g&'
    api_key = 'api_key=hpvZycW22qCjn5cRM1xtWB8NKq4dQ2My&'
    limit = 'limit=10'
    url_final = f'{url_first_part}{q}{rating}{api_key}'
    url_final_2 = f'{url_first_part}{q}{rating}{api_key}{limit}'
    # if url_final == url: # checking f-string
    #     print(url_final)
    # for dictionary in data['data']:
    #     print(dictionary)
    height_over_hundred = [item for item in data['data'] if int(item['images']['original']['height']) > 100]
    print(f'Number of the gifs with hegth over 100: {len(height_over_hundred)}')
    for dict in height_over_hundred:
        print(f'url: {dict["url"]}\n')



#Only return the first 10 gifs. Hint: In the Giphy Documentation, check out the relevant Request Parameters.
response2 = requests.get('https://api.giphy.com/v1/gifs/search?q=hilarious&rating=g&api_key=hpvZycW22qCjn5cRM1xtWB8NKq4dQ2My&limit=10')

if response2.status_code == 200:
    data = response2.json()
    print(len(data['data']))
    height_over_hundred = [item for item in data['data'] if int(item['images']['original']['height']) > 100]
    print(f'Number of the gifs with hegth over 100: {len(height_over_hundred)}')
    for dict in height_over_hundred:
        print(f'url: {dict["url"]}\n')

# #Exercise 3 : Giphy API #2
# term = input('Enter the term: ')
# url = f'https://api.giphy.com/v1/gifs/search?q=bulldog&api_key=hpvZycW22qCjn5cRM1xtWB8NKq4dQ2My'
# response3 = requests.get(url)
# if response3.status_code == 200:
#     data = response3.json()
#     print(len(data['data']))
#

