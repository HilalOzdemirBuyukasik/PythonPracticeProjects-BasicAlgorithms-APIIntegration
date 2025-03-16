import json
from requests import get
from pprint import pprint

import requests
from pprint import pprint

api_key = "key"
city = ("Marrakesh")
base_url = "http://api.weatherstack.com/current"

url = f"{base_url}?access_key={api_key}&query={city}"
response = requests.get(url)

data = response.json()

pprint(data)

#ekrana şehrin current temperature, current wind_speed ve location name değerlerini yazdıralım.

if response.status_code == 200 and 'current' in data:
    location_name = data['location']['name']

    current_temperature = data['current']['temperature']
    current_wind_speed = data['current']['wind_speed']

    print(f'City: {location_name}')
    print(f'Current Temperature: {current_temperature}°C')
    print(f'Current Wind Speed: {current_wind_speed} km/h')
else:
    print('Error: Could not retrieve data for the specified city.')

#searching mekanizması, ve Crud operasyonu yapın.

import requests

def search_weather(city):

    api_key = "key"
    base_url = "http://api.weatherstack.com/current"

    url = f'{base_url}?access_key={api_key}&query={city}'

    response = requests.get(url)

    data = response.json()

    if response.status_code == 200 and 'current' in data:
        location_name = data['location']['name']
        current_temperature = data['current']['temperature']
        current_wind_speed = data['current']['wind_speed']
        print(f'City: {location_name}')
        print(f'Current Temperature: {current_temperature}°C')
        print(f'Current Wind Speed: {current_wind_speed} km/h')
    else:
        print(f'Error: Could not retrieve data for the city: {city}')


city = input('Enter the city name to search the weather: ')
search_weather(city)


import requests

def get_weather(city):
    api_key = "key"

    base_url = "http://api.weatherstack.com/current"

    url = f'{base_url}?access_key={api_key}&query={city}'

    response = requests.get(url)

    data = response.json()

    if response.status_code == 200 and 'current' in data:
        location_name = data['location']['name']
        current_temperature = data['current']['temperature']
        current_wind_speed = data['current']['wind_speed']
        print(f'City: {location_name}')
        print(f'Current Temperature: {current_temperature}°C')
        print(f'Current Wind Speed: {current_wind_speed} km/h')
    else:
        print(f'Error: Could not retrieve data for {city}')
