from pyowm.owm import OWM
from pyowm.utils import timestamps
import matplotlib.pyplot as plt
import pytz
import datetime
import requests
owm = OWM('b46c6ebe45c5fcfe383273534cc2fbb8')
mgr = owm.weather_manager()
reg = owm.city_id_registry()

def get_id_city(city_name):
    url = f'http://api.openweathermap.org/data/2.5/find?&appid=b46c6ebe45c5fcfe383273534cc2fbb8'
    response = requests.get(url)
    data = response.json()
    for city in data['list']:
        if city['name'] == city_name:
            return city['id']

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


list_of_tuples = reg.ids_for('Tel Aviv', matching='like')
print(list_of_tuples)
print(list_of_tuples[1][1])
print(list_of_tuples[1][2])

def get_weather_info_v2():
    list_of_tuples = reg.ids_for('Tel Aviv', matching='exact')
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

def get_current_weather(location):
    observation = mgr.weather_at_id(location)
    weather = observation.weather
    return weather


# Function to get current wind information for a location
def get_wind_info(location):
    observation = mgr.weather_at_id(location)
    wind = observation.weather.wind()
    return wind


# Function to get today's sunrise and sunset times for a location
def get_sunrise_sunset(location):
    observation = mgr.weather_at_id(location)
    sunset_time = observation.weather.sunset_time('iso')
    sunrise_time = observation.weather.sunrise_time('iso')
    return sunrise_time, sunset_time


# Function to display weather information in a user-friendly way
def display_weather_info(location,name):
    weather = get_current_weather(location)
    wind = get_wind_info(location)
    sunrise, sunset = get_sunrise_sunset(location)

    print(f"Current weather in {name.capitalize()}: {weather.detailed_status}")
    print(f"Temperature: {weather.temperature('celsius')['temp']}°C")
    print(f"Wind speed: {wind['speed']} m/s")
    print(f"Wind direction: {wind['deg']}°")
    print(f"Sunrise time: {sunrise}")
    print(f"Sunset time: {sunset}")


# Function to ask user for location input
def get_user_location():
    location = input("Enter a city name: ")
    return location


# Main function to run the weather app
def main():
    location = get_user_location()
    list_of_tuples = reg.ids_for(location, matching='like')
    display_weather_info(list_of_tuples[0][0], location)


main()


def get_forecast_by_city_name(name):
    location = get_user_location()
    list_of_tuples = reg.ids_for(location, matching='like')
    name_of_the_city = list_of_tuples[1][1]
    country_of_the_city = list_of_tuples[1][2]
    observation = mgr.forecast_at_place(name_of_the_city,country_of_the_city,'3h')
    weather = observation.weather
    print(weather.detailed_status)

def get_air_pollution():
    mgr = owm.airpollution_manager()
    reg = owm.city_id_registry()
    location = get_user_location()
    list_of_tuples = reg.ids_for(location, matching='like')
    name_of_the_city = list_of_tuples[0][1]
    country = list_of_tuples[0][2]
    list_of_locations = reg.locations_for(name_of_the_city, country=country, matching='exact')
    city = list_of_locations[0]
    lat = city.lat
    lon = city.lon
    air_status = mgr.air_quality_at_coords(lat,lon)  # London, GB
    co = air_status.co
    no = air_status.no
    no2 = air_status.no2
    o3 = air_status.o3
    so2 = air_status.so2
    pm2_5 = air_status.pm2_5
    pm_10 = air_status.pm10
    nh_3 = air_status.nh3
    # and for air quality index
    aqi = air_status.aqi
    print(f'Air Quality: {aqi}. CO : {co}. NO : {no}, NO2:{no2}')

get_air_pollution()



# Mini_Project


def init_plot():
    plt.figure(figsize=(10, 6))
    plt.ylabel('Temperature (°C)')
    plt.title('Temperature and Humidity Forecast')


def plot_temperatures(forecast):
    dates = [weather.reference_time(timeformat='iso') for weather in forecast]
    temperatures = [weather.temperature('celsius')['temp'] for weather in forecast]
    humidity = [weather.humidity for weather in forecast]
    bars = plt.bar(dates, temperatures, color='blue')
    return bars, humidity

def write_humidity_on_bar_chart(bars, humidity):
    for bar, hum in zip(bars, humidity):
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2.0, yval, f'{hum}%', va='bottom')  # Add humidity values on top

def main(city='London',country='GB'):
    full_location = f"{city},{country}"
    forecast = mgr.forecast_at_place(full_location, '3h').forecast.weathers[:3]  # Example: Getting the first 8 forecasts

    init_plot()
    bars, humidity = plot_temperatures(forecast)
    write_humidity_on_bar_chart(bars, humidity)

    # Style adjustments
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()

    plt.show()


main()