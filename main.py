import modules.COLORS as COLORS
import modules.my_functions as functions
import modules.just_for_fun as just_for_fun
from modules.MyClasses import YaUploader

if __name__ == '__main__':

    # Задача 1. Выясняем кто из заднных супер-геров умнее
    supertoken = '2619421814940190'
    names = ['Hulk', 'Captain America', 'Thanos']
    print(f'{COLORS.RED}Task #1.{COLORS.WHITE} Who is smarted {", ".join(names)}?')

    status, result = functions.who_is_smarter(supertoken, names)

    if status is True:
        name, intelligence = result
        print(f'The smartest hero is {COLORS.GREEN}{name}{COLORS.WHITE} - '
              f'intelligence {COLORS.GREEN}{intelligence}{COLORS.WHITE}.\n')
    else:
        print(f'{COLORS.RED}failure: {COLORS.WHITE}{result}')

    # Задача 2. Загружаем файл на Яндекс.диск
    print(f'{COLORS.RED}Task #2.{COLORS.WHITE} Upload file to Yandex.disk')

    OAuth_token = '->place OAuth_token HERE<-'
    file_to_upload = 'upload/super_heroes_ids.json'

    uploader = YaUploader(OAuth_token)
    result = uploader.upload(file_to_upload)

    print(result)

    # Just for fun. Парсим https://superheroapi.com/ids.html
    # Получаем имена героев привязанных к id и сохраняем в словарь 'output/super_heroes_ids.json'
    print(f"{COLORS.RED}Just for fun #1.{COLORS.WHITE} "
          f"Collect super-heroes names & ids from https://superheroapi.com/ids.html")

    just_for_fun.get_super_heroes_ids('https://superheroapi.com/ids.html')