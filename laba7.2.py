import json
from itertools import product

import requests

url = f'https://api.hh.ru/vacancies'
#response = requests.get(url)
#print(response)
params = {
    "text": "python-разработчик",
    "area": 2  # санкт-петербург
}

# Выполняем GET-запрос
response = requests.get(url, params=params)
print(response)
# Проверяем статус ответа
if response.status_code == 200:
    data = response.json()

    
    for vacancy in data['items'][:6]:  # Выводим первые 6 вакансий
        print(f"ID: {vacancy['id']}")
        print(f"Название вакансии: {vacancy['name']}")
        print(f"Компания: {vacancy['employer']['name']}")
        print(f"Зарплата: {vacancy['salary']}")
        print(f"Ссылка на вакансию: {vacancy['alternate_url']}")
        print(f"Дата публикации: {vacancy['published_at']}")
        print("-" * 40)
else:
    print("Ошибка при получении данных:", response.status_code)

