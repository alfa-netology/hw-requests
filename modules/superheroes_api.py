import requests
import os
import json
from bs4 import BeautifulSoup

import modules.colors as COLORS

# Задача 1
def who_is_smarter(token: str, names: list):
    """ выесняет кто из героев умнее """
    print(f'{COLORS.RED}Task #1.{COLORS.WHITE} Who is smarted {", ".join(names)}?')

    intelligence, hero_intelligence = 0, 0
    smartest = ''
    for name in names:
        url = f'https://superheroapi.com/api/{token}/search/{name}'
        response = requests.get(url).json()

        if response['response'] == 'success':
            results = response['results']
            """
            на запрос по имени героя может прийти больше одного ответа.
            Hulk -> Hulk, Red Hulk, She-Hulk. Surprise! Surprise!
            поэтому фильтрую ответ в поиске нужного имени.
            """
            hero = [item for item in results if item['name'] == name]
            hero_intelligence = int(hero[0]['powerstats']['intelligence'])

            if intelligence < hero_intelligence:
                intelligence = hero_intelligence
                smartest = name

        elif response['response'] == 'error':
            return False, f"{response['error']}, name: {name}\n"

    return True, [smartest, intelligence]

# Just for fun
def get_ids_and_names(url):
    """
    парсит полученный HTML-код со страницы https://superheroapi.com/ids.html
    создает словарь {'hero_id': 'hero_name'} и сохраняет его в output/super_dict.json
    """
    print(f"{COLORS.RED}Just for fun #1.{COLORS.WHITE} "
          f"Parse super-heroes names & ids from https://superheroapi.com/ids.html")

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
