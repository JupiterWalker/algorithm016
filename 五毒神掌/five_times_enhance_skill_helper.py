# coding:utf-8
__author__ = 'cwang14'
import json
from pip._vendor.distlib.compat import raw_input
from datetime import datetime, timedelta

n = 5


def get_data(filename):
    print('从数据库获取数据...')
    with open(filename, 'r', encoding='utf-8') as file:
        data = json.load(file)
    print('从数据库获取数据成功')
    return data


def write_data(filename, data):
    with open(filename, 'w', encoding='utf-8') as f:
        print('正在存档...')
        json.dump(data, f, ensure_ascii=False)
        print('已存档！')


def record(data, specific_date=None):
    inputs = raw_input('记录哪几题(空格分割)？')
    problems = inputs.split(' ')
    if specific_date:
        today = specific_date
    else:
        today = get_today()
    offset = 1
    for i in range(n):
        date = today.strftime("%Y-%m-%d")
        data[date] = list({*data.setdefault(date, []), *problems})
        today = today + timedelta(days=offset)
        offset += 1
    write_data(filename, data)


def get_today():
    today = datetime.now()
    return today


def get_problem(data):
    today = get_today().strftime("%Y-%m-%d")
    print(data.get(today) if data.get(today) else '今天放假，无题可做！')


def list_problems(data):
    print("===================日程表===================")
    data = sorted(data.items())
    today = get_today()
    next_day = datetime.fromisoformat(data[0][0])
    for k, v in data:
        this_day = datetime.fromisoformat(k)
        if this_day != next_day:
            print(next_day.strftime("%Y-%m-%d" + ":"))
        msg = f'{k}:  {", ".join(v)}'
        if [this_day.year, this_day.month, this_day.day] == [today.year, today.month,
                                                             today.day]:
            msg = msg + "   <<<------------现在的位置"
        print(msg)
        next_day = this_day + timedelta(days=1)
    print("")


def make_up(data):
    date = raw_input('输入想要补录的日期(年-月-日)')
    year, month, day = map(int, date.strip().split('-'))
    specific_date = datetime(year, month, day)
    record(data, specific_date=specific_date)


if __name__ == '__main__':
    filename = 'database.json'
    data = get_data(filename)
    mapping = {'w': record, 'g': get_problem, 'l': list_problems, 'm': make_up}
    operation = ''
    while (operation) != 'q':
        operation = raw_input('w:记录 g:取出 l:查看日程 m:补记录>')
        if operation not in mapping:
            continue
        mapping[operation](data)
    print('欢迎下次光临～')