import requests
from bs4 import BeautifulSoup
import json
import os

import modules.COLORS as COLORS

def get_super_heroes_ids(url):
    """
    парсит полученный HTML-код со страницы https://superheroapi.com/ids.html
    создает словарь {'hero_id': 'hero_name'} и сохраняет его в output/super_dict.json
    """
    soup = get_html(url)
    items = soup.find_all('tr')
    super_heroes_ids_and_names = {}

    for item in items:
        id_ = item.find_all('td')[0].text
        name = item.find_all('td')[1].text
        super_heroes_ids_and_names[id_] = name

    result = json.dumps(super_heroes_ids_and_names, indent=4)
    save_name = os.path.join(os.getcwd(), 'output', 'super_heroes_ids.json')

    if os.path.isfile(save_name):
        os.remove(save_name)

    with open(os.path.join(save_name), 'a') as f:
        f.write(result)

    print(f"{COLORS.GREEN}Success:{COLORS.WHITE} data collected & saved\n{save_name}")

def get_html(url):
    """ возвращает HTML-код запрошенной страницы """
    response = requests.get(url)
    if response.ok:
        return BeautifulSoup(response.content, 'html.parser', from_encoding="UTF-8")
    else:
        return f'Не удалось получить исходный HTML-код со старинцы {url}'