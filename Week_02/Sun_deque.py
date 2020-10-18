# coding:utf-8
__author__ = 'cwang14'

from collections import deque
from timeit import timeit
import dis
import timeit
d = deque()
l = list()

def dque_append_demo():
    d.append(1)
    return

def list_demo():
    l.append(1)
    return

print(f'dque: {timeit.repeat(stmt=dque_append_demo, number=10000)}')
print(f'list: {timeit.repeat(stmt=list_demo, number=10000)}')
