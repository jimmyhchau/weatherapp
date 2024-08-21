import os
import requests
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Function to convert temperature from Celsius to Fahrenheit
def celsius_to_fahrenheit(celsius_temp):
    return (celsius_temp * 9 / 5) + 32

# Function to get the current weather data for a specific location
def get_current_weather(location, api_key):
    url = f'http://api.weatherstack.com/current?access_key={api_key}&query={location}'
    response = requests.get(url)
    data = response.json()

    # Print the full response for debugging
    print("API Response:", data)

    if 'current' in data:
        return data  # Return the entire data to handle both 'current' and 'location'
    else:
        raise ValueError('No current weather data available or error occurred')

# Main block
if __name__ == '__main__':
    api_key = os.getenv('WEATHER_API_KEY')
    # Get weather information for a specific city by changing location
    location = 'Los Angeles, CA'

    try:
        weather_data = get_current_weather(location, api_key)
        current_data = weather_data.get('current', {})
        location_data = weather_data.get('location', {})

        if current_data:
            temp_celsius = current_data.get('temperature', 0)
            temp_fahrenheit = celsius_to_fahrenheit(temp_celsius)
            description = current_data.get('weather_descriptions', ['No description'])[0]
            humidity = current_data.get('humidity', 0)
            utc_time = current_data.get('observation_time')
            local_time = location_data.get('localtime')

            print(f"Location: {location}")
            print(f"Temperature: {temp_fahrenheit} °F")
            print(f"Weather: {description}")
            print(f"Humidity: {humidity} %")
            print(f"Local Date and Time: {local_time}")
            print(f"UTC: {utc_time}")
        else:
            print("No weather data available.")
    except ValueError as e:
        print("Error:", e)
