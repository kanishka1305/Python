import requests


def get_weather_data(city_name):
    
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = base_url + "q=" + city_name + "&appid=" + api_key
    response = requests.get(complete_url)
    return response.json()


def display_weather_data(weather_data):
    if weather_data['cod'] != '404':
        main = weather_data['main']
        wind = weather_data['wind']
        weather_description = weather_data['weather'][0]['description']

        print(f"Temperature: {main['temp']}K")
        print(f"Humidity: {main['humidity']}%")
        print(f"Weather Description: {weather_description}")
        print(f"Wind Speed: {wind['speed']} m/s")
    else:
        print("City Not Found")


if __name__ == "__main__":
    location = input("Enter the city name: ")
    weather_data = get_weather_data(location)
    display_weather_data(weather_data)
