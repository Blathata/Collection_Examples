"""
Получение и анализ данных о погоде

Задача:
    Напишите код, который осуществляет GET-запрос к указанному API для получения погодных данных заданного города.
    Преобразовать полученный JSON-ответ в Python-объект с помощью метода response.json().
    Проанализировать данные и определить дату с самой минимальной температурой.
Сыылка на урок https://stepik.org/lesson/693007/step/6?thread=solutions&unit=692617
"""
import requests

# Функция для извлечения числового значения температуры из строки
def extract_temperature(temp_str):
    return int(temp_str.replace("°C", ""))

# Выполним GET-запрос к указанному URL
response = requests.get("https://parsinger.ru/3.4/1/json_weather.json")

# Проверим статус ответа
response.raise_for_status()

# Преобразуем JSON-ответ в список словарей
weather_data = response.json()

# Инициализируем переменные для хранения минимальной температуры и соответствующей даты
min_temperature = float('inf')
min_temperature_date = None

# Проходим по всем словарям в списке
for entry in weather_data:
    # Извлекаем температуру и дату из текущего словаря
    current_temperature = extract_temperature(entry["Температура воздуха"])
    current_date = entry["Дата"]

    # Обновляем минимальную температуру и соответствующую дату, если нужно
    if current_temperature < min_temperature:
        min_temperature = current_temperature
        min_temperature_date = current_date

# Выводим дату с минимальной температурой
print(f"Самая низкая температура: {min_temperature}°C, дата: {min_temperature_date}")