"""
Задача:
    Написать скрипт на Python, который выполнит GET-запрос к данному API для получения JSON-данных.
    Преобразовать полученный JSON-ответ в Python-объект с использованием метода response.json().
    Проанализировать древовидную структуру переписки и подсчитать количество сообщений, отправленных каждым участником.
{
'Anastasia': *, 'Vladimir': *, 'Yulia': *, 'Maria': *, 'Kirill': *, 'Anton': *, 'Petr': *, 'Dmitry': *, 'Olga': *, 
'Maxim': *, 'Elena': *, 'Alex': *, 'Natalia': *, 'Tatiana': *, 'Svetlana': *, 'Andrey': *, 'Sergey': *, 'Oksana': *,
'Ivan': *, 'Irina': *
}
Ссылка на задачу https://stepik.org/lesson/693007/step/7?thread=solutions&unit=692617
"""

import requests


# #Example_1
from collections import Counter
import re


response = requests.get('https://parsinger.ru/3.4/3/dialog.json')

match = r'"username": "(\w*)"'
answer = Counter(re.findall(match, response.text))

print(dict(sorted(answer.items(), key=lambda x: (-x[1], x[0]))))


#########################################################################################


#Example_2
res = {}

def add_message(data):
    """Функция сложения сообщений пользователя"""
    res[data['username']] = res.get(data['username'], 0) + 1
    return res

def sorted_dict(data):
    """Функция сортировки словаря по убыванию"""
    res = sorted(data.items(), key=lambda x: (-x[1], x[0]))
    return dict(res)

def count_users_message(data):
    """Функция переборки древа сообщений"""
    if data['comments']:
        add_message(data)
        for i in data['comments']:
            count_users_message(i)
    else:
        add_message(data)

count_users_message(response)

print(sorted_dict(res))