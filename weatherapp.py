import requests
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.environ.get('WEATHER_API_KEY')
base_url = "http://api.weatherapi.com/v1/current.json"
city = input("Enter city name: ")
parameters = {'key': api_key, 'q': city, 'units': 'metric'}

response = requests.get(base_url, parameters)

if response.status_code == 200:
    data = response.json()
    temperature = data['current']['temp_c']
    humidity = data['current']['humidity']
    description = data['current']['condition']['text']
    print(f"Temperature: {temperature}°C")
    print(f"Humidity: {humidity}%")
    print(f"Description: {description}")
else:
    print("Error in the HTTP request")

