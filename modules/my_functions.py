import requests

# Задача 1
def who_is_smarter(token: str, names: list):
    """ выесняет кто из героев умнее """
    intelligence = 0
    smartest = ''
    for name in names:
        url = f'https://superheroapi.com/api/{token}/search/{name}'
        response = requests.get(url).json()

        if response['response'] == 'success':
            results = response['results']
            """
            на запрос по имени героя может прийти больше одного ответа.
            Hulk -> Hulk, Red Hulk, She-Hulk. Surprise! Surprise!
            поэтому перебираю ответ в поиске нужного имени.
            """
            for item in results:
                if item['name'] == name:
                    hero_intelligence = int(item['powerstats']['intelligence'])

            if intelligence < hero_intelligence:
                intelligence = hero_intelligence
                smartest = name

        elif response['response'] == 'error':
            return False, f"{response['error']}, name: {name}"

    return True, [smartest, intelligence]
