import csv
import requests
from bs4 import BeautifulSoup

session = requests.Session()

url = 'https://parsinger.ru/html/index1_page_1.html'
site = 'https://parsinger.ru/html/'


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


def create_file(m: str, lst: list[str]):
    """Создает или записывает данные в файл формата csv

    Args:
        m (str): Атрибут для создания-перезаписи('w') или дополнеия файла('a')
        lst (list): Заголовки для столбцов таблицы
    """
    with open("Список часов.csv", mode=m, encoding="utf-8-sig", newline="") as file:
        writer = csv.writer(file, delimiter=";")
        writer.writerow(lst)


title = [
    'Наименование', 'Артикул', 'Бренд', 'Модель', 'Тип', 'Технология экрана',
    'Материал корпуса', 'Материал браслета', 'Размер', 'Сайт производителя',
    'Наличие', 'Цена', 'Старая цена', 'Ссылка на карточку с товаром']

create_file("w", title)


def pages()-> list[str]:
    """Возвращает список страниц для парсинга"""
    soup1 = soup(url)
    return [f"{site}{page['href']}" for page in soup1.find('div', class_="pagen").find_all('a')]


for page in pages():
    #получаем список артикулов на странице
    lst_articles = [i for i in soup(page).find_all('div', class_="sale_button")]
    # получаем ссылку на карту артикула
    link_card = [i['href'] for i in [i.select_one("[href]").attrs for i in lst_articles]]
    # создаем полную ссылку к карте артикула
    res = [i for i in [f'{site}{i}' for i in link_card]]
    for i in res:
        soup2 = soup(i)
        name = [i for i in soup2.find('p', id="p_header")]
        articles_num = [i.text.split(':')[1].strip() for i in soup2.find('p', class_="article")]
        descriptions = [i[1:] for i in [i.text.split('\n') for i in soup2.find_all('ul', id="description")]]
        in_stock = [i.split(':')[1].strip() for i in soup2.find('span', id="in_stock")]
        rate = [i for i in soup2.find('span', id="price")]
        old_rate = [i for i in soup2.find('span', id="old_price") ]
        link_card = [i]
        for  title, article, descr, quantity, price, old_price, link in zip(
            name, articles_num, descriptions, in_stock, rate, old_rate, link_card
            ):
            build_list =title, article, *[i.split(':')[1].strip() for i in descr if i], quantity, price, old_price, link
            create_file("a", build_list)
    print('Парсинг прошел отлично!')
