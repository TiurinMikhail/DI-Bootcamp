from pyowm.owm import OWM
import requests
owm = OWM('b46c6ebe45c5fcfe383273534cc2fbb8')
mgr = owm.weather_manager()
# reg = owm.city_id_registry()

# def get_id_city(city_name):
#     url = f'http://api.openweathermap.org/data/2.5/find?&appid=b46c6ebe45c5fcfe383273534cc2fbb8'
#     response = requests.get(url)
#     data = response.json()
#     for city in data['list']:
#         if city['name'] == city_name:
#             return city['id']
#
def get_city_id():
    try:
        response = requests.get('https://ipinfo.io/json')
        data = response.json()
        city = data.get('city')
        return city
    except Exception as e:
        print(f"Error: {e}")



def get_weather_info(city_name= 'Bat Yam,IL'):
    observation = mgr.weather_at_place(city_name)
    weather = observation.weather
    weather_description = weather.detailed_status
    tempepature = weather.temperature('celsius')['temp']
    wind = weather.wind()['speed']
    sunrise_time = weather.sunrise_time(timeformat='date')
    sunset_time = weather.sunset_time(timeformat='date')
    print(f'The weather for {city_name}: {weather_description}, temperature {tempepature} celsius degrees and wind {wind} meters per second')
    print(f'The sunrise in {city_name}: {sunrise_time}. Sunset: {sunset_time}.')

get_weather_info()

#
# list_of_tuples = london = reg.ids_for('Tel Aviv', matching='like')
# print(list_of_tuples)

def get_weather_info_v2():
    location = int(input('Enter the id of the city in which you would like to get weather: '))
    observation = mgr.weather_at_place(location)
    weather = observation.weather
    weather_description = weather.detailed_status
    tempepature = weather.temperature('celsius')['temp']
    wind = weather.wind()['speed']
    sunrise_time = weather.sunrise_time(timeformat='date')
    sunset_time = weather.sunset_time(timeformat='date')
    print(f'The weather for {location[:-3]}: {weather_description}, temperature {tempepature} celsius degrees and wind {wind} meters per second')
    print(f'The sunrise in {location[:-3]} in {sunrise_time}. Sunset in {sunset_time}.')
# get_weather_info_v2()