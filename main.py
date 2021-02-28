import modules.COLORS as COLORS
import modules.my_functions as functions
import modules.just_for_fun as just_for_fun

if __name__ == '__main__':

    # Задача 1. Выясняем кто из заднных супер-геров умнее
    print('Task #1')
    supertoken = '2619421814940190'
    names = ['Hulk', 'Captain America', 'Thanos']

    status, result = functions.who_is_smarter(supertoken, names)

    if status is True:
        name, intelligence = result
        print(f'The smartest hero is {COLORS.GREEN}{name}{COLORS.WHITE} - '
              f'intelligence {COLORS.GREEN}{intelligence}{COLORS.WHITE}.\n')
    else:
        print(f'{COLORS.RED}failure: {COLORS.WHITE}{result}')

    # Just for fun. Парсим https://superheroapi.com/ids.html
    # Получаем имена героев привязанных к id и сохраняем в словарь 'output/super_heroes_ids.json'
    print("Just for fun #1. Collect super-heroes names & ids from https://superheroapi.com/ids.html")
    just_for_fun.get_super_heroes_ids('https://superheroapi.com/ids.html')