import requests
import os
import json
import time

from collections import defaultdict
from datetime import date

import modules.COLORS as COLORS

# Задача #3
def get_questions(days: int, tags: str):
    """
    получает список вопросов со stackoverflow
        args:
            days(int) : кол-во дней вычитаемых из текущей даты, чтобы получить fromdate
            tags(str) : тэг по которому отбираются вопросы
    """
    questions_raw = defaultdict(list)  # временный словарь, для сохранения вопросов с каждой страницы
    page_number = 1
    questions = {}  # словарь для сохранения результата
    todate_stamp = int(time.time())
    fromdate_stamp = todate_stamp - (days * 86400)

    # отправляю запрос
    page_data = make_request(fromdate_stamp, todate_stamp, tags, page_number)
    if page_data is not False:
        # собираю вопросы с первой страницы выдачи
        questions_raw['questions'].append(page_data['items'])
        print(f'Collect data from page {page_number}')

        # если в ответе больше одной страницы (has_more=True), то перебираю все
        while page_data['has_more'] is True:
            page_number += 1
            page_data = make_request(fromdate_stamp, todate_stamp, tags, page_number)
            if page_data is not False:
                questions_raw['items'].append(page_data['items'])
                print("\033[A                             \033[A")
                print(f'Collect data from page {page_number}')

        # можно было сохранить questions_raw сразу в том виде, что он есть,
        # но я хочу свою структуру словаря, где ключ порядковый номер(counter) новости,
        # а его значения все атрибуты новости, которые мне нужны.
        counter = 1
        for page in questions_raw['items']:
            for question in page:
                questions[str(counter)] = {
                    'creation_date': str(date.fromtimestamp(question['creation_date'])),
                    'question_id': question['question_id'],
                    'title': question['title'],
                    'link': question['link'],
                    'tags': question['tags']
                }
                counter += 1
        print("\033[A                             \033[A")
        print(f"Total questions collected: {COLORS.GREEN}{counter-1}{COLORS.WHITE}")

    # сохраняю результат
    if len(questions) > 0:
        file_ = os.path.join(os.getcwd(), 'output', 'stackoverflow_questions.json')
        print(f"{COLORS.GREEN}Success:{COLORS.WHITE} questions collected & saved")
        print(file_, '\n')

        with open(file_, 'w', encoding='utf-8') as file:
            file.write(json.dumps(questions, indent=4))
    else:
        print(f'{COLORS.RED}Nothing to save.{COLORS.WHITE}')


def make_request(fromdate: int, todate: int, tags: str, page_number: int):
    url = 'https://api.stackexchange.com/2.2/questions'

    params = {
        'fromdate': fromdate,
        'todate': todate,
        'order': 'asc',
        'sort': 'activity',
        'tagged': tags,
        'pagesize': 100,
        'page': page_number,
        'site': 'stackoverflow',
        'filter': '!4(L6lo0Or0WtBtOxT'  # фильтр, получаю только creation_date, question_id, title, link, tags
    }

    response = requests.get(url, params=params)
    if response.ok:
        return response.json()
    else:
        print(f'Response code <{response.status_code}>')
        print(f"<Error {response.json()['error_id']}> {response.json()['error_message']}.")
        return False
