import modules.COLORS as COLORS
import modules.superheroes_api as superheroes_api
from modules.yandex_api import YaUploader
import modules.stackoverflow_api as stackoverflow_api

if __name__ == '__main__':

    # Задача 1. Выясняем кто из заднных супер-геров умнее
    super_token = '2619421814940190'
    names = ['Hulk', 'Captain America', 'Thanos']
    status, result = superheroes_api.who_is_smarter(super_token, names)

    if status is True:
        name, intelligence = result
        print(f'The smartest hero is {COLORS.GREEN}{name}{COLORS.WHITE} - '
              f'intelligence {COLORS.GREEN}{intelligence}{COLORS.WHITE}.\n')
    else:
        print(f'{COLORS.RED}Failure: {COLORS.WHITE}{result}')

    # Задача 2. Загружаем файл на Яндекс.диск
    print(f'{COLORS.RED}Task #2.{COLORS.WHITE} Upload file to Yandex.disk')

    OAuth_token = '->place OAuth_token HERE<-'
    file_to_upload = 'upload/super_heroes_ids.json'

    uploader = YaUploader(OAuth_token)
    result = uploader.upload(file_to_upload)
    print(result)

    # Задача 3. Получить со stackoverflow список вопросов за последние 2 дня с тэгом python.
    # результат сохраняется 'output/stackoverflow_questions.json'
    # третий параметр для вызова имя сайта с кого собирать сведения, по умолчанию stackoverflow
    stackoverflow_api.get_questions(1, 'Python')
    stackoverflow_api.get_questions(1, 'Python', 'ru.stackoverflow')

    # Just for fun.
    # Парсим имена и id героев https://superheroapi.com/ids.html
    # результат сохраняется 'output/super_heroes_ids.json'
    superheroes_api.get_ids_and_names('https://superheroapi.com/ids.html')
