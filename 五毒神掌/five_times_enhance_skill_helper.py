# coding:utf-8
__author__ = 'cwang14'

import json
import random

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
    inputs = raw_input('记录哪一题？').replace(" ", "")
    problems = [inputs]
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
    if not data:
        print("")
        return
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


def enhance_memory(data):
    today = datetime.now()
    thirty_days_ago = today - timedelta(days=30)
    old_problems = []

    for date_str, problems in data.items():
        problem_date = datetime.fromisoformat(date_str)
        if problem_date < thirty_days_ago:
            old_problems.extend(problems)
    from termcolor import colored

    print("")
    print("")
    print("==================================================")
    if old_problems:
        selected_problem = random.choice(old_problems)

        print(colored("          加强记忆题目: ", "cyan", attrs=["bold"]) + colored(selected_problem, "red",
                                                                                    attrs=["bold",
                                                                                           "underline"]))
    else:
        print(colored("          没有找到 30 天之前的题目！", "red", attrs=["bold"]))

    print("==================================================")
    print("")
    print("")


if __name__ == '__main__':
    from termcolor import colored

    filename = './五毒神掌/database_new_travel.json'
    data = get_data(filename)
    mapping = {'w': record, 'g': get_problem, 'l': list_problems, 'm': make_up, 'e': enhance_memory}
    operation = ''
    date = sorted(data.items())
    from termcolor import colored


    def print_banner():
        print(colored("=" * 50, "green"))
        print(colored(" " * 10, "green") + colored("欢迎使用", "cyan", attrs=["bold"]) + colored("五毒神掌", "red",
                                                                                                 attrs=["bold",
                                                                                                        "underline"]))
        print(colored("=" * 50, "green"))


    print_banner()
    # get how many days I keep doing this
    today = get_today()
    start_date = datetime.fromisoformat(date[0][0])
    keep_days = (today - start_date).days
    today = today.strftime("%Y-%m-%d")
    if today in date:
        print("今天已经记录过了哦！")
    else:
        print("今天还没有记录哦！")
    print(f"从{date[0][0]}开始，你已经坚持了{keep_days}天")
    while (operation) != 'q':
        operation = raw_input('w:记录 g:取出 l:查看日程 m:补记录 e:加强记忆>')
        if operation not in mapping:
            continue
        mapping[operation](data)
    print('欢迎下次光临～')
