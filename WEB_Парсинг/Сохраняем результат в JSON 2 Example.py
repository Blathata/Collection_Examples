import csv
import requests
import json
from bs4 import BeautifulSoup

session = requests.Session()



def soup(url: str)-> (BeautifulSoup | Exception):
    """Функция принемает url, проверяет статус, декодирует, обрабатывает в парсере

    Args:
        url: Принемает url для обработки

    Returns:
        Возвращает обработанный HTML или XML-документ
    """
    try:
        response = session.get(url=url)
        response.encoding = "utf-8"
        if response.status_code == 200:
            return BeautifulSoup(response.text, "lxml")
    except Exception as e:
        print(f' >>>>>>> Ошибка:{e}, страница не найдена')


soup1 = soup('https://parsinger.ru/html/index1_page_1.html')
pages = [i.get('href') for i in [i for i in soup1.find('div', class_="pagen").find_all('a')]]
category_page = [i.get('href') for i in [i for i in soup1.find('div', class_="nav_menu").find_all('a')]]

lstresult_json = []


for cat_page in range(1, len(category_page)+1):
    for i in range(1, len(pages)+1):
        soup2 = soup(f'https://parsinger.ru/html/index{cat_page}_page_{i}.html')
        name = [i.text.strip() for i in soup2.find_all('a', class_="name_item")]
        descriptions = [i.text.strip().split('\n') for i in soup2.find_all('div', class_="description")]
        rate = [i.text.strip() for i in soup2.find_all('p', class_="price")]
        for title, descr, price in zip(name, descriptions, rate):
            lstresult_json.append({
            "Наименование": title,
            descr[0].split(':')[0].strip(): descr[0].split(':')[1].strip(),
            descr[1].split(':')[0].strip(): descr[1].split(':')[1].strip(),
            descr[2].split(':')[0].strip(): descr[2].split(':')[1].strip(),
            descr[3].split(':')[0].strip(): descr[3].split(':')[1].strip(),
            "Цена": price
            })

with open('res.json', 'w', encoding='utf-8') as file:
    json.dump(lstresult_json, file, indent=4, ensure_ascii=False)

print('Сбор данных окончен')
