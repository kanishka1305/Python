import requests

api_key = "f6373f38cb150275ff49b91798ee64de"
def get_weather_data(city_name):
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = base_url + "q=" + city_name + "&appid=" + api_key
    response = requests.get(complete_url)
    return response.json()

def display_weather_data(weather_data):
    if weather_data['cod'] != '404':
        if 'main' in weather_data:
            main = weather_data['main']
            print(f"Temperature: {round(main['temp']-273.15)}°C")
            print(f"Humidity: {main['humidity']}%")
        else:
            print("Temperature and Humidity data not available")
        if 'wind' in weather_data:
            wind = weather_data['wind']
            print(f"Wind Speed: {wind['speed']} m/s")
        else:
            print("Wind Speed data not available")
        if 'weather' in weather_data:
            weather_description = weather_data['weather'][0]['description']
            print(f"Weather Description: {weather_description}")
        else:
            print("Weather Description data not available")
    else:
        print("City Not Found")

if __name__ == "__main__":
    location = input("Enter the city name: ")
    weather_data = get_weather_data(location)
    display_weather_data(weather_data)
