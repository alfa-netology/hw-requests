import modules.my_functions as functions
import modules.COLORS as COLORS

if __name__ == '__main__':

    supertoken = '2619421814940190'
    names = ['Hulk', 'Captain America', 'Thanos']

    status, result = functions.who_is_smarter(supertoken, names)

    if status is True:
        name, intelligence = result
        print(f'The smartest hero is {COLORS.GREEN}{name}{COLORS.WHITE} - '
              f'intelligence {COLORS.GREEN}{intelligence}{COLORS.WHITE}.\n')
    else:
        print(f'{COLORS.RED}failure: {COLORS.WHITE}{result}')