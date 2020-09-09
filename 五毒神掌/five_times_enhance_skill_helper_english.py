# coding:utf-8
__author__ = 'cwang14'
import json
from pip._vendor.distlib.compat import raw_input
from datetime import datetime, timedelta

n = 5


def get_data(filename):
    print('get data from database...')
    with open(filename, 'r', encoding='utf-8') as file:
        data = json.load(file)
    print('get data success!')
    return data


def write_data(filename, data):
    with open(filename, 'w', encoding='utf-8') as f:
        print('saving...')
        json.dump(data, f, ensure_ascii=False)
        print('saved！')


def record(data):
    inputs = raw_input('what you learn today(split by space)？')
    problems = inputs.split(' ')
    today = get_today()
    offset = 1
    for i in range(n):
        today = today + timedelta(days=offset)
        date = today.strftime("%Y-%m-%d")
        data[date] = list({*data.setdefault(date, []), *problems})
        offset += 1
    write_data(filename, data)


def get_today():
    today = datetime.now()
    return today


def get_problem(data):
    today = get_today().strftime("%Y-%m-%d")
    print(data.get(today) if data.get(today) else 'nothing to do today！')


def list_problems(data):
    print("=======calender=======")
    for k, v in data.items():
        print(f'{k}:  {", ".join(v)}')
    print("")


if __name__ == '__main__':
    filename = 'database.json'
    data = get_data(filename)
    mapping = {'w': record, 'g': get_problem, 'l': list_problems}
    while (operation := raw_input('(w)write (g)get (l)list calender >')) != 'q':
        if operation not in mapping:
            continue
        mapping[operation](data)
    print('see you next time～')