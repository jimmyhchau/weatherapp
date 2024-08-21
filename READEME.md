# Weather Python Application

This Python app displays current weather temperature, location, humidity, and descriptions.

# Getting Started
This app requires Python installed and a weatherstack API key.

1. Download Python at python.org
2. Sign up at weatherstack.com for a free API key

# How to use
Follow these steps to use this application
1. Download the project files in your computer.
2. Set up the API key
````
2a. Create a file at root directory and name it ".env" (e.g. right click C:\Users\...\PycharmProjects\WeatherVisualization and select new file and name it .env)
2b. In the new .env file type: WEATHER_API_KEY='' 
2c. Copy paste your personal API key into WEATHER_API_KEY='<paste here>' 
````
3. Download Python packages in terminal
````
pip install -r requirements.txt
````
4. In the program, weather_visualization.py line 30, change the city to get current weather descriptions 

# Example input and output
Input:
````
location = 'Los Angeles, CA'
````
Output:
````
Location: Los Angeles, CA
Temperature: 82.4 °F
Weather: Sunny
Humidity: 55 %
Local Date and Time: 2024-08-21 11:24
UTC: 06:24 PM
````