import json
import requests
def get_weather(city_name):

    url = f'http://api.openweathermap.org/data/2.5/weather?q=Vologda&appid=2f44ab8d94825710392977b37c24d3ac&units=metric'
    response = requests.get(url) #получение инфы с сервер

    if response.status_code == 200:
        data = response.json()  # Преобразуем ответ в JSON
        temperature = data['main']['temp']  # Температура
        humidity = data['main']['humidity']  # Влажность
        pressure = data['main']['pressure']  # Давление

        print(f"Погода в городе {city_name}:")
        print(f"Температура: {temperature}°C")
        print(f"Влажность: {humidity}%")
        print(f"Давление: {pressure} гПа")
    else:
        print("Ошибка при получении данных:", response.status_code)


city_name = 'Вологда'

get_weather(city_name)